const path = require('path');
const TerserPlugin = require('terser-webpack-plugin');

const here = path.resolve(__dirname);

module.exports = {
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
  },
  output: {
    path: path.resolve(here, 'umd'),
    library: 'Seamless',
    libraryTarget: 'umd',
    libraryExport: 'default',
  },
  optimization: {
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          format: {
            comments: false,
          },
        },
        extractComments: false,
      }),
    ],
  },
}