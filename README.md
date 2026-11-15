# DBMS Vault

Past BCSE302L Database Systems FAT questions, shelved by module and by paper.
Static site: one `index.html`, no build tools, no dependencies.

## Files
- `index.html`  the finished site (this is what gets deployed)
- `src/template.html`  page layout, styles and scripts
- `src/data.json`  all questions, modules and papers (83 questions, 8 papers)
- `build.py`  injects data.json into the template to produce index.html

## Editing questions
1. Open `src/data.json`, fix or add a question under `"questions"`.
2. Run `python3 build.py`
3. Commit and push; Vercel redeploys automatically.

## Push to GitHub
```bash
cd dbms-vault-site
git init
git add .
git commit -m "DBMS Vault"
git branch -M main
git remote add origin https://github.com/<your-username>/dbms-vault.git
git push -u origin main
```
Create the empty `dbms-vault` repository on github.com first (no README, no .gitignore).

## Host on Vercel
1. Go to vercel.com, sign in with GitHub, click **Add New > Project**.
2. Import the `dbms-vault` repository.
3. Framework Preset: **Other**. Leave Build Command and Output Directory empty. Root Directory: `./`.
4. Click **Deploy**. You get a `*.vercel.app` link; every push to `main` redeploys.

Or with the CLI: `npm i -g vercel`, then run `vercel --prod` inside the folder.
