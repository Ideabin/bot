# Ideabin Bot

The repository contains bots that perform various automation tasks for our Ideabin service (which aims at creating a store of ideas that anyone can use/work upon.)

There are two simple bots right now:

### Iqra

It fetches users from the registration repository and adds them to the database.

It also fetches new Github Gists of all the users tagged with #ideabin and adds them to the databse.

### Ziqra

It tweets fifteen un-tweeted ideas every time it runs.

A limit has been placed so that we don't accidently cross Twitter tweet limits.

### Azeema

This bot will watch our Twitter account for any new mentions and will auto reply to them.

## Todo

We've thought of one more bot that we still have to do:

### Bushra

This bot will send out dail or weekly mails (to the people who want them) which will contain a summary of ideas that have been added during that period.

@akifkhan suggested the use of Send Grid's API to send mails, so we could look into it.
