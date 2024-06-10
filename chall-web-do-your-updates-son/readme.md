## Flag 🚩 

STHACK{procfs_and_locatedb_are_my_best_friendz}

## Principe 💭 

### Do Your Updates Son

> I know I should update my infra... But man these cartoons are just the best, I can't get my eyes off it! Well, at least my db stores them all so I can watch them anytime now! ^.^

- Medium / Web / Linux
- Sources are given
    - Remove the `Detail` from the readme
    - Censor the `flag_random_path` in `docker compose.yml`
---

```bash
# Setup or Change Flag
sed -i -E 's#.*./flag:/flag/.*#      - ./flag:/flag/flag_random_path_bimbamboumeuuuu:ro#g' docker compose.yml

# Setup
docker compose down --remove-orphans --volumes ; docker compose up --build --remove-orphans -d

# Recheck
docker compose run --rm -it --volume "$PWD:/host" -w /host --entrypoint /bin/bash mlflow -x exploit.sh

# Logs
docker compose logs -f

# Light-Long Auto-Fix
echo '*/30 * * * * root bash -c "cd /opt/sthack-2024-challs/do-your-updates-son ; docker compose run --rm -it --volume /opt/sthack-2024-challs/do-your-updates-son:/host -w /host --entrypoint /bin/bash mlflow -x exploit.sh ; docker compose down --remove-orphans --volumes ; docker compose up --build --remove-orphans -d"' | sudo tee -a /etc/crontab

# Doc / Source
# https://huntr.com/bounties/1fe8f21a-c438-4cba-9add-e8a5dab94e28
```

## Configuration 🛠 

1 host or VM with 2+ cores and ideally docker installed, only port 80 required

## Write-up 📝 

- Abuse mlflow (see the nice huntrdev writeup from mizu)
- Read `/var/cache/locate/locatedb` and extract the flag path
- Read the flag with the same exploit

Refer to `# Setup & Recheck` for auto-exploit & live checks! :)

## Contact 📲 

laluka
