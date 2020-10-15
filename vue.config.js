const path = require("path");

module.exports = {
  outputDir: "frontend/dist",
  assetsDir: "frontend/static",
  // baseUrl: IS_PRODUCTION
  // ? 'http://cdn123.com'
  // : '/',
  // For Production, replace set baseUrl to CDN
  // And set the CDN origin to `yourdomain.com/static`
  // Whitenoise will serve once to CDN which will then cache
  // and distribute
  devServer: {
    proxy: {
      "/api*": {
        // Forward frontend dev server request for /api to django dev server
        target: "http://localhost:8000/",
      },
    },
  },
  configureWebpack: {
    resolve: {
      alias: {
        "@": path.join(__dirname, "frontend"),
      },
    },
    entry: {
      app: path.join(__dirname, "frontend", "main.js"),
    },
  },
};
