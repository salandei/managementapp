# OSFF User Management App

## Project Description

OSFF User Management App is designed for any
form of organization to effectively manage the
various Departments, Roles, and Members of the
organization.

*Note: We are yet to include an option for only administrators.*

### Database Schema

The database consists of three tables: users, roles, and departments.
- Each User can be assigned a role and a department
- A Role can be assigned to at least one User
- A Department consists of User(s) with the same/different Role(s)


## How to run the app locally

**Note: It is advisable to create a Python virtual environment before installing dependencies.**

- clone the repo to your local machine
- cd into project's root
- run `pip install -r requirements.txt` to install necessary dependencies
- run `python main.py` to get the app configured and running
- access the app on http://localhost:5000



# Multi-model CRUD App

Design and build a web application using Flask or Express.

## Requirements

Your application

- must use Flask or Express
- must use a relational database 
- must have multiple, related database models
- must have features to Create, Read, Update, and Delete some of those models from a web interface
- must be designed such that it works properly on different devices (desktop and mobile)

You must also include a README.md file that
- explains what your app does
- explains the tables in your schema
- explains how to set the app up and run it locally

## Optional components

The following are optional, but not required:

- you may use an ORM library
- you may use a CSS framework
- you may use an API
- you may have users and authentication
- you may use  a library to manage authentication and authorization
- you may deploy your application to the web

## Recommendations

The possibilities for your application are wide and varied. Choosing a scope for your project that you can complete within the time is key.

Before you start coding, you should:
- write out a list of pages in your planned application
- write the routes associated with those pages and their actions
- write out the plan for the models in your schema

You are also highly encouraged to build a scoped-down **Minimum Viable Product** (MVP) first, then add more features after you have it working.

## Notes

- If you choose to start from a Flask or Express starter code template (like [flask-starter](https://github.com/ksh7/flask-starter) or [express-postgres-boilerplate](https://github.com/mateo-io/express-postgres-boilerplate)) you **must** mention it in your README file.
