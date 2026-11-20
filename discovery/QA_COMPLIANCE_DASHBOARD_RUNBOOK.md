---
title: "QA Compliance Dashboard — Operational Runbook"
date: "2026-07-06"
version: "1.0.0"
audience: ["QA Lead", "DevOps", "OnCall Engineer"]
sla: "Response < 4h if alerts triggered"
---

# QA Compliance Dashboard — Operational Runbook

## 🎯 Purpose

Real-time monitoring of APB application quality across three dimensions:
1. **Test Coverage** (Sonar) — target 85%, warning 80%, critical <70%
2. **Bug Status** (Sonar + Jira) — high/critical bugs, resolution time
3. **Dependencies** (Dependabot) — open vulnerabilities, time-to-fix

**Users:** QA Leads (daily), DevOps (on-demand), Architecture Review Board (weekly reviews)

---

## 📊 Dashboard Overview

### Pages

| Page | Purpose | Frequency | Owner |
|------|---------|-----------|-------|
| **Overview** | Trend metrics, quality summary | Real-time | QA Lead |
| **By Environment** | DEV/PRE/PROD breakdown | Real-time | DevOps |
| **Deployments** | Pre-deploy quality gates | On-demand | Release Manager |

---

## 🔴 Alert Thresholds & Response

### Alert 1: Coverage Drop (High severity)
**Trigger:** Average coverage < 80%

**What it means:**
- One or more applications dropped below warning threshold
- Likely cause: new code merged without adequate tests, or deletion of test files

**Your action (within 4 hours):**
1. Go to **Overview page** → Coverage trend chart
2. Identify which application dropped
3. Check Sonar project page (link in dashboard)
4. **Identify root cause:**
   - New untested code? → require PR revert or test coverage PR
   - Deleted tests? → investigate with development team
   - Test framework misconfiguration? → notify CI/CD team
5. **Create Jira ticket** (if not auto-created): `QA-XXX: Investigate coverage drop in [APP]`
6. **SLA:** Ticket triaged and root cause identified within 4 hours

---

### Alert 2: Critical Vulnerability (Critical severity)
**Trigger:** OpenVulnerabilities > 0 (Critical severity)

**What it means:**
- Dependabot detected a critical vulnerability in a dependency
- Application cannot deploy to PROD until resolved

**Your action (immediate, within 1 hour):**
1. Go to **Overview page** → Dependabot table
2. Identify affected application and dependency
3. Check Dependabot alert in GitHub (link: `https://github.com/portdebarcelona/[repo]/security/dependabot`)
4. **Assess impact:**
   - Is the vulnerability exploitable in your app? (check code usage)
   - Can you upgrade the dependency? (check for breaking changes)
5. **Options:**
   - **If fixable:** Create PR to upgrade dependency, run tests, merge
   - **If not fixable:** Approve Dependabot's automated PR (if available)
   - **If risky:** Document exception, escalate to Security team
6. **SLA:** Resolved or exception approved within 24 hours

---

### Alert 3: Bug Resolution Delay (Medium severity)
**Trigger:** Mean Time to Close > 7 days

**What it means:**
- Bugs detected by Sonar are taking too long to fix
- Suggests backlog pressure or lower priority assignment

**Your action (within 24 hours):**
1. Go to **By Environment page** → Resolution Time chart
2. Filter by your team
3. For each application > 7 days average:
   - Review open bugs in Jira (link: `https://jira.atlassian.net/...`)
   - Prioritize critical/high bugs
   - Reassign or add to current sprint if possible
4. **Escalation:** If cannot be resolved within sprint, notify Architecture

---

## 📋 Weekly Review Checklist

**Day:** Every Friday, 10:00 UTC  
**Attendees:** QA Lead, DevOps, Architecture (30 min)

```
[ ] Review Overview page — coverage trend OK? (should be ≥85%)
[ ] Review By Environment page — any DEV/PRE/PROD divergence?
[ ] Review Deployments page — all apps green? Any blockers?
[ ] Check Jira → open QA tickets → any stale issues?
[ ] Check GitHub Dependabot → any old PRs still open?
[ ] Confirm all alerts were triaged
[ ] Document findings in Jira (ticket: QA-WEEKLY-[date])
```

---

## 🔧 Dashboard Maintenance

### Data Sources & Refresh Schedule

| Source | Frequency | Lag | Owner |
|--------|-----------|-----|-------|
| **Sonar** | Daily, 02:00 UTC | <1 hour | CI/CD |
| **Dependabot** | Daily, 02:15 UTC | <1 hour | CI/CD |
| **Jira** | Hourly | <15 min | CI/CD |
| **GitHub** | On-demand | Immediate | CI/CD |

### Troubleshooting Missing Data

#### Sonar data missing?
1. Check Sonar job status: `sonar.apb.internal` → Projects → [app] → Job status
2. If failed: check SonarQube logs `/opt/sonarqube/logs/sonarqube.log`
3. Contact CI/CD team if persistent

#### Dependabot data missing?
1. Check GitHub repo settings: Settings → Security & analysis → Dependabot enabled?
2. If disabled: enable & run manual scan
3. Check for rate limiting: GitHub → Settings → Developer settings → Personal tokens

#### Jira data missing?
1. Verify Jira API connectivity: `curl -u user:token https://portdebarcelona.atlassian.net/rest/api/3/myself`
2. Check token expiration: Azure Key Vault → `jira-api-token` → expiry date
3. If token expired: generate new one + update AKV

---

## 📈 Performance & Cost

### Typical Query Performance
- Overview dashboard: **<5 sec** (cached data)
- By Environment: **5-10 sec** (filtered queries)
- Deployments: **10-15 sec** (multi-table join)

### Cost Estimate (Power BI/Grafana)
- **Power BI:** ~€50/month (1 Pro license for report author)
- **Grafana:** ~€0 (self-hosted) or ~€50/month (Grafana Cloud)

### Optimization Tips
1. Set Sonar refresh to **daily** (not hourly) to reduce API calls
2. Archive data > 90 days to Cosmos DB
3. Use **column-level security** in Power BI if multi-team access

---

## 🚨 Emergency Procedures

### Dashboard Down?
1. Check dashboard service status (Power BI → Service health / Grafana → Status page)
2. If data source unavailable: use **Sonar directly** (`sonar.apb.internal`)
3. If Jira unavailable: manually query GitHub Dependabot alerts
4. **Escalation:** Notify Architecture + CI/CD within 15 min

### Suspected Data Integrity Issue?
1. Compare dashboard metrics vs. source systems manually (Sonar, Jira)
2. If discrepancy > 5%: pause dashboard, investigate
3. **Do NOT make decisions** based on dashboard until verified

---

## 📞 Escalation & Support

| Issue | Contact | Response Time |
|-------|---------|----------------|
| Coverage alert | QA Lead | <4h |
| Vulnerability alert | Security Team | <1h |
| Dashboard down | DevOps | <30 min |
| Data discrepancy | CI/CD Team | <2h |

---

## 📝 Change Log

| Date | Change | Who |
|------|--------|-----|
| 2026-07-06 | Initial version 1.0 | Claude Code |
| TBD | Add performance metrics | TBD |
| TBD | Add SAST scanning integration | TBD |

---

## 🎓 Common Questions

**Q: Why is my app showing 0% coverage?**  
A: Sonar was never configured for this app. Ask DevOps to add it to CI/CD pipeline.

**Q: Can I deploy if alerts are active?**  
A: No. Green light requires:
- Coverage ≥ 80%
- High+Critical bugs < 5
- No Critical vulnerabilities
Check Deployments page before release.

**Q: How often should I check the dashboard?**  
A: Daily (QA Lead), on-demand (DevOps), weekly (Architecture). Set calendar reminders.

**Q: Can I customize alerts?**  
A: Yes, via Grafana alerts or Power BI alerts settings. Contact CI/CD team for changes.

---

*For issues or questions, contact QA Lead or escalate to Architecture.*

**Last Updated:** 2026-07-06  
**Status:** ✅ Operational  
**Generated by:** Claude Code — APB AI Framework
