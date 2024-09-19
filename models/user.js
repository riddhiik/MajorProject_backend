const { DataTypes, Model } = require('sequelize');
const sequelize = require('../db'); // Import the Sequelize instance

class User extends Model { }

// Define the User model
User.init(
    {
        id: {
            type: DataTypes.INTEGER,
            autoIncrement: true,
            primaryKey: true,
        },
        user_name: {
            type: DataTypes.STRING,
            allowNull: false,
        },
        password: {
            type: DataTypes.STRING,
            allowNull: false,
        },
        created_at: {
            type: DataTypes.DATE,
            defaultValue: DataTypes.NOW,
        },
        updated_at: {
            type: DataTypes.DATE,
            defaultValue: DataTypes.NOW,
        },
    },
    {
        sequelize, // Passing the `sequelize` instance
        modelName: 'User', // The name of the model (table name in the DB)
        tableName: process.env.USER_TABLE, // Using environment variable for table name
        timestamps: true, // Automatically manage `created_at` and `updated_at`
        underscored: true, // If you prefer `created_at` over `createdAt`
    }
);

module.exports = User;
