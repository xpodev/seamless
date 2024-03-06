const path = require('path');
const TersePlugin = require('terser-webpack-plugin');

const staticPath = path.resolve(__dirname, 'src/jsx/server/static');

module.exports = {
  entry: `./ts/main.ts`,
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
    alias: {
      '~': staticPath,
    },
  },
  output: {
    filename: 'main.js',
    path: staticPath
  },
  optimization: {
    minimizer: [
      new TersePlugin({
        terserOptions: {
          format: {
            comments: false,
          },
        },
        extractComments: false,
      }),
    ],
  },
};