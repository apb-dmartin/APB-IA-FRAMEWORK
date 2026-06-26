/**
 * Forge Function: APB AI Framework Invoker
 *
 * Intermediario entre Rovo y el APB AI Framework API (Azure APIM).
 * Esta función se ejecuta en el runtime Atlassian Forge (Node.js).
 *
 * PENDIENTE DE IMPLEMENTACIÓN POR EL EQUIPO DE DESARROLLO APB:
 * - Completar la autenticación OAuth 2.0 contra Azure AD APB
 * - Gestionar el ciclo de vida del token (caché + renovación)
 * - Implementar el polling de jobs asincrónos
 * - Añadir logging de auditoría (quién invocó qué agente y cuándo)
 *
 * Referencia: adapter-rovo-v1.0.md, openapi/apb-framework-api.yaml
 */

import Resolver from "@forge/resolver";
import api, { fetch } from "@forge/api";

const resolver = new Resolver();

const FRAMEWORK_API_URL =
  process.env.APB_FRAMEWORK_API_URL ||
  "https://apim.portdebarcelona.cat/ai-framework/v1";

/**
 * Obtiene un token OAuth 2.0 de Azure AD para llamar al Framework API.
 * PENDIENTE: implementar caché del token (válido 1h típicamente).
 */
async function getFrameworkToken() {
  // TODO: implementar Client Credentials flow contra Azure AD APB
  // Credenciales gestionadas como Forge secrets (APB_FRAMEWORK_CLIENT_SECRET)
  throw new Error(
    "getFrameworkToken: pendiente de implementación por equipo de Plataforma APB"
  );
}

/**
 * Invoca un agente del framework y hace polling hasta obtener el resultado.
 */
resolver.define("invokeAgent", async ({ payload, context }) => {
  const { agentId, userRequest, projectKey, deliveryChannel } = payload;

  // TODO: descomentar cuando getFrameworkToken esté implementado
  // const token = await getFrameworkToken();

  const requestBody = {
    user_request: userRequest,
    context: {
      source: projectKey ? "jira" : "description",
      project_key: projectKey,
    },
    delivery: {
      channel: deliveryChannel || "inline",
      sharepoint_path: "/sites/Arquitectura/Artefactos-IA/",
    },
    user_id: context.accountId,
  };

  // TODO: añadir Authorization: Bearer ${token} cuando esté implementado
  const invokeResponse = await fetch(
    `${FRAMEWORK_API_URL}/agents/${agentId}/invoke`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // "Authorization": `Bearer ${token}`,
      },
      body: JSON.stringify(requestBody),
    }
  );

  if (!invokeResponse.ok) {
    throw new Error(`Framework API error: ${invokeResponse.status}`);
  }

  const job = await invokeResponse.json();

  // Polling simplificado — en producción usar webhook o cola de eventos
  // para no bloquear el hilo de la Forge Function
  let attempts = 0;
  const maxAttempts = 30; // máx 60s de espera (30 * 2s)

  while (attempts < maxAttempts) {
    await new Promise((resolve) => setTimeout(resolve, 2000));

    const statusResponse = await fetch(
      `${FRAMEWORK_API_URL}/agents/${agentId}/jobs/${job.job_id}`,
      {
        headers: {
          // "Authorization": `Bearer ${token}`,
        },
      }
    );

    const status = await statusResponse.json();

    if (status.status === "completed") {
      return {
        result: status.result,
        human_review_required: status.result.human_review_required,
        review_checklist: status.result.review_checklist || [],
      };
    }

    if (status.status === "failed") {
      throw new Error(
        `Agente ${agentId} falló: ${status.error?.message || "error desconocido"}`
      );
    }

    attempts++;
  }

  throw new Error(
    `Timeout esperando respuesta del agente ${agentId} (>60s). El job ${job.job_id} puede seguir en curso — consultar estado en ${job.status_url}`
  );
});

export const handler = resolver.getDefinitions();
