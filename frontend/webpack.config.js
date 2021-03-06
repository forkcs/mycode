const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: {
        login: './app/src/scripts/login.js',
        register: './app/src/scripts/register.js',
        problems_student: './app/src/scripts/problems_student.js',
        style: './app/src/styles/app.scss'
    },
    output: {
        path: path.resolve(__dirname, './app/static'),
        filename: 'js/[name].min.js'
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
        })
    ]
};
