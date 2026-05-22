# Deployment Guide for CHRONO-ARCH

## Documentation Deployment

```bash
cd docs/
mkdocs build
mkdocs gh-deploy
```

Netlify Deployment

```bash
netlify deploy --prod
```

Verification

```bash
curl https://chrono-arch.netlify.app
```

