const webpack = require('webpack');
//var babelEnv = require('@babel/preset-env')

const config = {
    entry:  __dirname + '/js/index.jsx',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
        rules: [
            {
                test: /\.jsx?/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react']
                    }
                }
            },
            {
                    test: /\.css$/,
                    loader:[ 'style-loader', 'css-loader' ]
                  }
        ]
    }
};
module.exports = config;
