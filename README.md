# docker-deployer

Inspired by GFGSREBLR

```
docker run -d --restart=unless-stopped -v /run:/run --name deploy --env OVERLORD_URL=https://deploy.davao.io/api/deploy/instance wfong/docker-deploy
```