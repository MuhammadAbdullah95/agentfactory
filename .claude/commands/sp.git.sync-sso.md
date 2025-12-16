---
description: Force push main branch to sso-sync remote (panaversity-global/sso-sync.git)
---

# SSO Sync Command

Force push the current main branch to the `sso-sync` remote at `https://github.com/panaversity-global/sso-sync.git`.

## Execution Steps

1. **Verify Remote Exists**
   ```bash
   git remote -v | grep sso-sync
   ```
   If `sso-sync` remote doesn't exist, add it:
   ```bash
   git remote add sso-sync https://github.com/panaversity-global/sso-sync.git
   ```

2. **Verify Current Branch**
   ```bash
   git rev-parse --abbrev-ref HEAD
   git log --oneline -3
   ```

3. **Force Push to sso-sync**
   ```bash
   git push sso-sync main --force
   ```

4. **Report Result**
   Report the sync status:
   - Commit hash pushed
   - Success/failure status
   - Any warnings

## Notes

- This command always force pushes, overwriting any divergent history on sso-sync
- Only syncs the `main` branch
- Remote URL: `https://github.com/panaversity-global/sso-sync.git`
