const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: [
        './app/src/index.js',
        './app/src/styles/app.scss'
    ],
    output: {
        path: path.resolve(__dirname, './app/public_html'),
        filename: 'js/index.min.js'
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/i,
                exclude: /node_modules/,
                use: [
                    {
                        loader: 'babel-loader'
                    }
                ]
            },
            {
                test: /\.s[ac]ss$/i,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'sass-loader'
                ]
            }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'css/app.min.css'
        }),
        new HtmlWebpackPlugin({
            template: './app/src/index.php',
            filename: 'index.php',
            publicPath: '/'
        })
    ]
};
