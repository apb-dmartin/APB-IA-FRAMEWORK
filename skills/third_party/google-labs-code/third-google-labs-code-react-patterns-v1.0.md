---
id: "third-google-labs-code-react-patterns-v1.0"
name: "React Component Patterns (Stitch)"
description: "Genera, valida y optimiza componentes React con TypeScript siguiendo diseño atómico, design systems, performance y testing."
version: "1.0.0"
status: "approved"
owner: "Arquitectura APB <arquitectura@portdebarcelona.cat>"
domain: "development"
created_date: "2026-06-22"
review_date: "2026-06-22"
autonomy_level: 1
source_repo: "https://github.com/google-labs-code/stitch-skills"
source_license: "MIT"
source_commit: "unverified"
verified_date: "2026-06-23"
---

# SKILL_DEV_DEVEXPRESS_FRONT — React Component Engineering

## 1. Propósito y Alcance

Esta skill extiende el conocimiento de Google Labs Stitch Skills para crear
componentes React production-ready con énfasis en:

- **TypeScript**: Tipado estricto, interfaces claras, generics apropiados
- **Design Systems**: Atomic Design, componentes composables, tokens de diseño
- **Performance**: Memoization, lazy loading, code splitting, virtualization
- **Testing**: Unit tests, integration tests, visual regression, a11y
- **Accessibility**: WCAG 2.1 AA, keyboard navigation, screen readers
- **Modern Patterns**: Hooks, Server Components, Suspense, Error Boundaries

**Casos de uso:**
1. Conversión de diseños (Figma, Sketch, Stitch) a componentes React
2. Implementación de design systems (tokens, theming, component library)
3. Refactorización de componentes legacy a modern patterns
4. Optimización de performance (bundle size, render cycles, lazy loading)
5. Establecimiento de convenciones de frontend para equipos

## 2. Arquitectura de Componentes

### 2.1 Atomic Design (Brad Frost)

```
atoms/           → Button, Input, Label, Icon (indivisible)
molecules/       → SearchBar (Input + Button + Icon), FormField (Label + Input + Error)
organisms/       → Header (Logo + Nav + SearchBar), ProductCard (Image + Title + Price + Button)
templates/       → HomepageTemplate, ProductPageTemplate (layout sin datos reales)
pages/           → Homepage, ProductPage (templates + datos reales)
```

### 2.2 Estructura de Componente

```typescript
// ✅ Componente bien estructurado: separación de concerns
// atoms/Button/Button.tsx
import React, { forwardRef, memo } from 'react';
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '@/lib/utils'; // Tailwind merge utility

// 1. Variant definition (design tokens)
const buttonVariants = cva(
  // Base styles (always applied)
  'inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-primary text-primary-foreground hover:bg-primary/90',
        destructive: 'bg-destructive text-destructive-foreground hover:bg-destructive/90',
        outline: 'border border-input bg-background hover:bg-accent hover:text-accent-foreground',
        secondary: 'bg-secondary text-secondary-foreground hover:bg-secondary/80',
        ghost: 'hover:bg-accent hover:text-accent-foreground',
        link: 'text-primary underline-offset-4 hover:underline',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-11 rounded-md px-8',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
);

// 2. TypeScript interface (explicit, documented)
export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean; // Polymorphic component support
  isLoading?: boolean;
  loadingText?: string;
}

// 3. Component implementation (forwardRef for composability)
export const Button = memo(forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, isLoading, loadingText, children, disabled, ...props }, ref) => {
    const Comp = asChild ? React.Slot : 'button';

    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        disabled={disabled || isLoading}
        aria-busy={isLoading}
        {...props}
      >
        {isLoading && (
          <span className="mr-2" aria-hidden="true">
            <LoadingSpinner className="h-4 w-4 animate-spin" />
          </span>
        )}
        {isLoading && loadingText ? loadingText : children}
      </Comp>
    );
  }
));

Button.displayName = 'Button';

// 4. Barrel export
export { buttonVariants };
export default Button;
```

### 2.3 Componente Compuesto (Compound Component Pattern)

```typescript
// ✅ Compound components: flexible composition, implicit state sharing
// organisms/Select/Select.tsx
import React, { createContext, useContext, useState, useCallback } from 'react';

// Context for implicit state sharing
interface SelectContextValue {
  value: string;
  onChange: (value: string) => void;
  isOpen: boolean;
  setIsOpen: (open: boolean) => void;
}

const SelectContext = createContext<SelectContextValue | null>(null);

const useSelect = () => {
  const context = useContext(SelectContext);
  if (!context) throw new Error('Select parts must be used within Select');
  return context;
};

// Root component
interface SelectProps {
  value: string;
  onChange: (value: string) => void;
  children: React.ReactNode;
}

export const Select: React.FC<SelectProps> & {
  Trigger: typeof SelectTrigger;
  Content: typeof SelectContent;
  Item: typeof SelectItem;
} = ({ value, onChange, children }) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleChange = useCallback((newValue: string) => {
    onChange(newValue);
    setIsOpen(false);
  }, [onChange]);

  return (
    <SelectContext.Provider value={{ value, onChange: handleChange, isOpen, setIsOpen }}>
      <div className="relative">{children}</div>
    </SelectContext.Provider>
  );
};

// Trigger
const SelectTrigger: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { isOpen, setIsOpen } = useSelect();

  return (
    <button
      type="button"
      onClick={() => setIsOpen(!isOpen)}
      aria-expanded={isOpen}
      aria-haspopup="listbox"
      className="..."
    >
      {children}
    </button>
  );
};

// Content (dropdown)
const SelectContent: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { isOpen } = useSelect();
  if (!isOpen) return null;

  return (
    <ul role="listbox" className="absolute z-50 ...">
      {children}
    </ul>
  );
};

// Item
const SelectItem: React.FC<{ value: string; children: React.ReactNode }> = ({ value, children }) => {
  const { value: selectedValue, onChange } = useSelect();
  const isSelected = selectedValue === value;

  return (
    <li
      role="option"
      aria-selected={isSelected}
      onClick={() => onChange(value)}
      className={cn('...', isSelected && 'bg-accent')}
    >
      {children}
    </li>
  );
};

// Attach sub-components
Select.Trigger = SelectTrigger;
Select.Content = SelectContent;
Select.Item = SelectItem;

// Usage
<Select value={theme} onChange={setTheme}>
  <Select.Trigger>Select theme</Select.Trigger>
  <Select.Content>
    <Select.Item value="light">Light</Select.Item>
    <Select.Item value="dark">Dark</Select.Item>
    <Select.Item value="system">System</Select.Item>
  </Select.Content>
</Select>
```

## 3. Performance Optimization

### 3.1 Memoization Strategy

```typescript
// ✅ Memoization hierarchy: prevent unnecessary re-renders
import React, { memo, useMemo, useCallback } from 'react';

// 1. Component memoization (for pure components)
const ExpensiveList = memo(function ExpensiveList({ items, onSelect }: Props) {
  return (
    <ul>
      {items.map(item => (
        <ListItem key={item.id} item={item} onSelect={onSelect} />
      ))}
    </ul>
  );
});

// 2. Value memoization (for expensive computations)
const Dashboard = ({ data, filter }: Props) => {
  const filteredData = useMemo(() => {
    return data.filter(item => item.matches(filter)).sort((a, b) => b.score - a.score);
  }, [data, filter]); // Only recompute when data or filter changes

  // 3. Callback memoization (for stable references passed to children)
  const handleSelect = useCallback((id: string) => {
    console.log('Selected:', id);
  }, []); // Stable reference, never recreates

  return <ExpensiveList items={filteredData} onSelect={handleSelect} />;
};

// 4. Context optimization (split contexts to prevent unnecessary re-renders)
// ❌ Bad: Single context with state + dispatch
// ✅ Good: Separate contexts
const StateContext = createContext<State>(null!);
const DispatchContext = createContext<Dispatch>(null!);

// Components consuming only dispatch don't re-render on state changes
const Toolbar = () => {
  const dispatch = useContext(DispatchContext); // Stable reference
  return <button onClick={() => dispatch({ type: 'RESET' })}>Reset</button>;
};
```

### 3.2 Code Splitting y Lazy Loading

```typescript
// ✅ Route-based code splitting
import React, { Suspense, lazy } from 'react';
import { ErrorBoundary } from '@/components/ErrorBoundary';

// Lazy load pages
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Settings = lazy(() => import('./pages/Settings'));
const Analytics = lazy(() => import('./pages/Analytics'));

// Loading fallback with skeleton
const PageSkeleton = () => (
  <div className="animate-pulse space-y-4">
    <div className="h-8 bg-gray-200 rounded w-1/3" />
    <div className="h-64 bg-gray-200 rounded" />
  </div>
);

// Router with Suspense boundaries
const App = () => (
  <ErrorBoundary fallback={<ErrorPage />}>
    <Suspense fallback={<PageSkeleton />}>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/settings" element={<Settings />} />
        <Route path="/analytics" element={<Analytics />} />
      </Routes>
    </Suspense>
  </ErrorBoundary>
);

// ✅ Component-level lazy loading (below the fold)
const HeavyChart = lazy(() => import('./components/HeavyChart'));

const Dashboard = () => {
  const [showChart, setShowChart] = useState(false);

  return (
    <div>
      <button onClick={() => setShowChart(true)}>Show Analytics</button>
      {showChart && (
        <Suspense fallback={<ChartSkeleton />}>
          <HeavyChart />
        </Suspense>
      )}
    </div>
  );
};
```

### 3.3 Virtualization (Large Lists)

```typescript
// ✅ Virtualization for lists > 100 items
import { useVirtualizer } from '@tanstack/react-virtual';

const VirtualList = ({ items }: { items: Item[] }) => {
  const parentRef = useRef<HTMLDivElement>(null);

  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50, // Average row height
    overscan: 5, // Render 5 extra items for smooth scrolling
  });

  return (
    <div ref={parentRef} className="h-400px overflow-auto">
      <div style={{ height: `${virtualizer.getTotalSize()}px`, position: 'relative' }}>
        {virtualizer.getVirtualItems().map(virtualItem => (
          <div
            key={virtualItem.key}
            style={{
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: `${virtualItem.size}px`,
              transform: `translateY(${virtualItem.start}px)`,
            }}
          >
            <ListItem item={items[virtualItem.index]} />
          </div>
        ))}
      </div>
    </div>
  );
};
```

## 4. Server Components (Next.js App Router)

### 4.1 Server vs. Client Components

```typescript
// ✅ Server Component (default in App Router): no 'use client'
// app/products/page.tsx
import { ProductGrid } from '@/components/ProductGrid';
import { getProducts } from '@/lib/api';

// Fetch data on server (no JS bundle impact)
export default async function ProductsPage() {
  const products = await getProducts(); // Direct DB/API call, no client fetch

  return (
    <main>
      <h1>Products</h1>
      {/* Server Component: rendered on server, HTML to client */}
      <ProductGrid products={products} />
    </main>
  );
}

// ✅ Client Component (interactivity needed): 'use client' directive
// components/AddToCartButton.tsx
'use client';

import { useState } from 'react';
import { addToCart } from '@/lib/cart';

export const AddToCartButton = ({ productId }: { productId: string }) => {
  const [isAdding, setIsAdding] = useState(false);

  const handleClick = async () => {
    setIsAdding(true);
    await addToCart(productId);
    setIsAdding(false);
  };

  return (
    <Button onClick={handleClick} isLoading={isAdding}>
      Add to Cart
    </Button>
  );
};

// ✅ Composition: Server Component wraps Client Component
// components/ProductCard.tsx (Server Component)
import { AddToCartButton } from './AddToCartButton';

export const ProductCard = ({ product }: { product: Product }) => (
  <article>
    <img src={product.image} alt={product.name} />
    <h2>{product.name}</h2>
    <p>{product.price}</p>
    {/* Client Component for interactivity */}
    <AddToCartButton productId={product.id} />
  </article>
);
```

### 4.2 Streaming y Suspense

```typescript
// ✅ Streaming with Suspense boundaries
// app/page.tsx
import { Suspense } from 'react';
import { ProductSkeleton } from '@/components/ProductSkeleton';
import { ReviewSkeleton } from '@/components/ReviewSkeleton';

export default function ProductPage() {
  return (
    <main>
      {/* Immediate render (no wait) */}
      <ProductHeader />

      {/* Stream in when ready */}
      <Suspense fallback={<ProductSkeleton />}>
        <ProductDetails />
      </Suspense>

      {/* Stream reviews independently */}
      <Suspense fallback={<ReviewSkeleton />}>
        <ProductReviews />
      </Suspense>

      {/* Stream recommendations independently */}
      <Suspense fallback={<RecommendationSkeleton />}>
        <RelatedProducts />
      </Suspense>
    </main>
  );
}
```

## 5. Design Tokens y Theming

### 5.1 Tailwind CSS Config

```typescript
// tailwind.config.ts
import type { Config } from 'tailwindcss';

const config: Config = {
  darkMode: ['class'], // Class-based dark mode
  content: ['./src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      // Design tokens mapped to CSS variables
      colors: {
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        primary: {
          DEFAULT: 'hsl(var(--primary))',
          foreground: 'hsl(var(--primary-foreground))',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary))',
          foreground: 'hsl(var(--secondary-foreground))',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive))',
          foreground: 'hsl(var(--destructive-foreground))',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted))',
          foreground: 'hsl(var(--muted-foreground))',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent))',
          foreground: 'hsl(var(--accent-foreground))',
        },
        popover: {
          DEFAULT: 'hsl(var(--popover))',
          foreground: 'hsl(var(--popover-foreground))',
        },
        card: {
          DEFAULT: 'hsl(var(--card))',
          foreground: 'hsl(var(--card-foreground))',
        },
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
      fontFamily: {
        sans: ['var(--font-sans)', 'system-ui', 'sans-serif'],
        mono: ['var(--font-mono)', 'monospace'],
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
};

export default config;
```

### 5.2 CSS Variables (Theming)

```css
/* globals.css - Light theme (default) */
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --card: 0 0% 100%;
  --card-foreground: 222.2 84% 4.9%;
  --popover: 0 0% 100%;
  --popover-foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
  --secondary: 210 40% 96.1%;
  --secondary-foreground: 222.2 47.4% 11.2%;
  --muted: 210 40% 96.1%;
  --muted-foreground: 215.4 16.3% 46.9%;
  --accent: 210 40% 96.1%;
  --accent-foreground: 222.2 47.4% 11.2%;
  --destructive: 0 84.2% 60.2%;
  --destructive-foreground: 210 40% 98%;
  --border: 214.3 31.8% 91.4%;
  --input: 214.3 31.8% 91.4%;
  --ring: 222.2 84% 4.9%;
  --radius: 0.5rem;
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

/* Dark theme */
.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
  --card: 222.2 84% 4.9%;
  --card-foreground: 210 40% 98%;
  /* ... inverted colors */
}
```

## 6. Testing Strategy

### 6.1 Unit Tests (Vitest/Jest)

```typescript
// Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';
import { vi } from 'vitest';

describe('Button', () => {
  it('renders with correct text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument();
  });

  it('handles click events', () => {
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Click</Button>);
    fireEvent.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('is disabled when loading', () => {
    render(<Button isLoading>Loading</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
    expect(screen.getByRole('button')).toHaveAttribute('aria-busy', 'true');
  });

  it('applies variant classes', () => {
    render(<Button variant="destructive">Delete</Button>);
    expect(screen.getByRole('button')).toHaveClass('bg-destructive');
  });

  it('forwards ref correctly', () => {
    const ref = { current: null as HTMLButtonElement | null };
    render(<Button ref={ref}>Ref</Button>);
    expect(ref.current).toBeInstanceOf(HTMLButtonElement);
  });
});
```

### 6.2 Integration Tests (Playwright/Cypress)

```typescript
// product-page.spec.ts (Playwright)
import { test, expect } from '@playwright/test';

test('user can add product to cart', async ({ page }) => {
  // Arrange
  await page.goto('/products/123');

  // Act
  await page.getByRole('button', { name: 'Add to Cart' }).click();

  // Assert
  await expect(page.getByRole('alert')).toHaveText('Product added to cart');
  await expect(page.getByTestId('cart-count')).toHaveText('1');
});

test('product page loads within performance budget', async ({ page }) => {
  await page.goto('/products/123');

  // Performance assertions
  const loadTime = await page.evaluate(() => performance.now());
  expect(loadTime).toBeLessThan(3000); // 3s budget

  // Lighthouse-like checks
  const lcp = await page.evaluate(() =>
    new PerformanceObserver((list) => {
      const entries = list.getEntries();
      return entries[entries.length - 1].startTime;
    }).observe({ entryTypes: ['largest-contentful-paint'] })
  );
});
```

### 6.3 Visual Regression (Chromatic/Storybook)

```typescript
// Button.stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  component: Button,
  tags: ['autodocs'],
  argTypes: {
    variant: {
      control: 'select',
      options: ['default', 'destructive', 'outline', 'secondary', 'ghost', 'link'],
    },
    size: {
      control: 'select',
      options: ['default', 'sm', 'lg', 'icon'],
    },
  },
};

export default meta;
type Story = StoryObj<typeof Button>;

export const Default: Story = {
  args: {
    children: 'Button',
  },
};

export const Destructive: Story = {
  args: {
    variant: 'destructive',
    children: 'Delete',
  },
};

export const Loading: Story = {
  args: {
    isLoading: true,
    loadingText: 'Saving...',
    children: 'Save',
  },
};

export const AllVariants: Story = {
  render: () => (
    <div className="flex gap-4">
      <Button>Default</Button>
      <Button variant="destructive">Destructive</Button>
      <Button variant="outline">Outline</Button>
      <Button variant="secondary">Secondary</Button>
      <Button variant="ghost">Ghost</Button>
      <Button variant="link">Link</Button>
    </div>
  ),
};
```

## 7. Accessibility (a11y)

### 7.1 ARIA y Semántica

```typescript
// ✅ Accessible form with proper ARIA
const LoginForm = () => {
  const [errors, setErrors] = useState<Record<string, string>>({});

  return (
    <form aria-labelledby="login-heading" noValidate>
      <h1 id="login-heading">Login</h1>

      <div className="space-y-4">
        <div>
          <label htmlFor="email">Email</label>
          <input
            id="email"
            type="email"
            name="email"
            aria-required="true"
            aria-invalid={errors.email ? 'true' : 'false'}
            aria-describedby={errors.email ? 'email-error' : undefined}
            required
          />
          {errors.email && (
            <span id="email-error" role="alert" className="text-destructive">
              {errors.email}
            </span>
          )}
        </div>

        <div>
          <label htmlFor="password">Password</label>
          <input
            id="password"
            type="password"
            name="password"
            aria-required="true"
            aria-invalid={errors.password ? 'true' : 'false'}
            aria-describedby={errors.password ? 'password-error' : undefined}
            required
          />
          {errors.password && (
            <span id="password-error" role="alert" className="text-destructive">
              {errors.password}
            </span>
          )}
        </div>

        <button type="submit">Login</button>
      </div>
    </form>
  );
};
```

### 7.2 Keyboard Navigation

```typescript
// ✅ Keyboard-accessible dropdown
const Dropdown = ({ items }: { items: string[] }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [focusedIndex, setFocusedIndex] = useState(-1);
  const buttonRef = useRef<HTMLButtonElement>(null);
  const listRef = useRef<HTMLUListElement>(null);

  const handleKeyDown = (e: KeyboardEvent) => {
    if (!isOpen) return;

    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        setFocusedIndex(i => Math.min(i + 1, items.length - 1));
        break;
      case 'ArrowUp':
        e.preventDefault();
        setFocusedIndex(i => Math.max(i - 1, 0));
        break;
      case 'Home':
        e.preventDefault();
        setFocusedIndex(0);
        break;
      case 'End':
        e.preventDefault();
        setFocusedIndex(items.length - 1);
        break;
      case 'Escape':
        e.preventDefault();
        setIsOpen(false);
        buttonRef.current?.focus();
        break;
      case 'Tab':
        setIsOpen(false);
        break;
    }
  };

  useEffect(() => {
    if (isOpen && focusedIndex >= 0) {
      listRef.current?.children[focusedIndex]?.focus();
    }
  }, [focusedIndex, isOpen]);

  return (
    <div>
      <button
        ref={buttonRef}
        onClick={() => setIsOpen(!isOpen)}
        aria-expanded={isOpen}
        aria-haspopup="listbox"
      >
        Select
      </button>
      {isOpen && (
        <ul ref={listRef} role="listbox" onKeyDown={handleKeyDown}>
          {items.map((item, index) => (
            <li
              key={item}
              role="option"
              tabIndex={-1}
              aria-selected={index === focusedIndex}
            >
              {item}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};
```

## 8. Checklist de Componente

### Diseño y Arquitectura
- [ ] ¿Sigue Atomic Design (atom, molecule, organism, template, page)?
- [ ] ¿Es composable (compound pattern, render props, slots)?
- [ ] ¿Separa concerns (presentation, logic, data)?
- [ ] ¿Es reusable (no hardcoded data, configurable via props)?
- [ ] ¿Sigue design system (tokens, variants, consistent naming)?

### TypeScript
- [ ] ¿Props interface documentada con JSDoc?
- [ ] ¿Tipos estrictos (no any, unknown usado apropiadamente)?
- [ ] ¿Generics usados para flexibilidad (Table<T>, List<T>)?
- [ ] ¿forwardRef para composabilidad con form libraries?
- [ ] ¿displayName para debugging (DevTools)?

### Performance
- [ ] ¿memo para componentes puros con props estables?
- [ ] ¿useMemo para computaciones costosas?
- [ ] ¿useCallback para handlers pasados a children?
- [ ] ¿Lazy loading para componentes below the fold?
- [ ] ¿Virtualization para listas > 100 items?
- [ ] ¿Code splitting por ruta y feature?
- [ ] ¿No re-renders innecesarios (React DevTools Profiler)?

### Accessibility
- [ ] ¿Semántica HTML correcta (button vs. div, nav, main, article)?
- [ ] ¿ARIA attributes apropiados (role, aria-label, aria-describedby)?
- [ ] ¿Keyboard navigation completo (tab, enter, escape, arrows)?
- [ ] ¿Focus management visible y lógico?
- [ ] ¿Color contrast ratio >= 4.5:1 (WCAG AA)?
- [ ] ¿Screen reader tested (NVDA, VoiceOver, JAWS)?
- [ ] ¿Reduced motion respetado (prefers-reduced-motion)?

### Testing
- [ ] ¿Unit tests para lógica y rendering?
- [ ] ¿Integration tests para user flows?
- [ ] ¿Visual regression tests (Storybook + Chromatic)?
- [ ] ¿a11y tests (axe-core, Lighthouse)?
- [ ] ¿Performance tests (Lighthouse CI, Web Vitals)?
- [ ] ¿Cross-browser tests (Chrome, Firefox, Safari, Edge)?

## 9. Anti-patrones de Frontend (Qué NO hacer)

- **Div soup**: Usar div para todo en lugar de elementos semánticos
- **Inline styles**: Styles hardcodeados en lugar de design tokens
- **Prop drilling**: Pasar props a través de 5+ niveles (usar Context)
- **useEffect abuse**: Lógica de negocio en useEffect en lugar de event handlers
- **No error boundaries**: App crashea completamente por error en componente
- **No loading states**: Usuario no sabe si la app está cargando
- **No empty states**: Pantalla en blanco cuando no hay datos
- **Z-index wars**: Valores arbitrarios de z-index (usar sistema de capas)
- **Magic numbers**: Padding/margin hardcodeados (usar spacing scale)
- **No responsive**: Diseño solo desktop (mobile-first approach)
- **No dark mode**: No respetar preferencia del sistema (os-class)
- **Bundle bloat**: Importar librerías completas en lugar de tree-shakeable

## 10. Integración con otras Skills APB

- **SKILL_DEV_CODE_BASE**: SOLID, DDD (componentes como entities con comportamiento)
- **SKILL_DEV_API_STANDARD**: GraphQL/REST data fetching (Apollo Client, React Query)
- **SKILL_DEV_REVIEW_ADVANCED**: Performance-expert agent para optimización de renders
- **SKILL_PLAT_CICD**: Frontend CI/CD (build, test, Lighthouse CI, deploy)
- **SKILL_OPS_OBSERVABILITY**: Web Vitals monitoring, error tracking (Sentry)
- **SKILL_ARCH_EVENT_DRIVEN**: Real-time updates (WebSocket, SSE, GraphQL subscriptions)
- **SKILL_GOV_STANDARDS**: Accessibility compliance (WCAG, ADA)

## 11. Referencias

- [google-labs-code/stitch-skills - react-components](https://github.com/google-labs-code/stitch-skills)
- [React Documentation](https://react.dev/)
- [Next.js App Router](https://nextjs.org/docs/app)
- [Tailwind CSS](https://tailwindcss.com/)
- [shadcn/ui](https://ui.shadcn.com/)
- [Atomic Design - Brad Frost](https://atomicdesign.bradfrost.com/)
- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [Playwright](https://playwright.dev/)
- [Storybook](https://storybook.js.org/)
- [Web Vitals](https://web.dev/vitals/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [A11y Project Checklist](https://www.a11yproject.com/checklist/)
