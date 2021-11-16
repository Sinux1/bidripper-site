# Setting up for Developers

These instructions are for a linux environment, specifically for an Ubuntu 20.04 fresh install.  

## Required packages

Some basics just in case (curl and git are the most important)

`sudo apt update -y && sudo apt upgrade -y && sudo apt autoremove && sudo apt install curl gcc make perl git python3-pip pipenv -y && pip3 install --user pipenv`  


## Make sure AWS CLI v2 is installed

Navigate to your home directory and install the AWS CLI
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
source ~/.bashrc
```

## Configure AWS profile

To deploy Bidripper you must have an AWS account, and it is highly recommended that you creater a user that is **not** the root user of the AWS account. Follow this link to create an AWS account. Once your account is created, create an admin user and save the account keys provided to you in a safe place because you will need them!

[Create a free AWS account and Admin User](https://docs.aws.amazon.com/translate/latest/dg/setting-up.html)


Once your AWS account is set up, get your (secret) access keys ready and then run in terminal

`aws configure`

Follow the questions. When asked enter `us-west-2` for region, and `json` for the question about return data types. This will configure a *_default_* profile that will be used later when pulling the amplify project.  

## Install nvm, npm, and node

From whatever directory  you installed aws cli, run

```bash
curl -sL "https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.0/install.sh" -o install_nvm.sh
bash install_nvm.sh
```

You can close and reopen your terminal like an amateur for this to take effect or run  

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

Sanity Check
`nvm --version` should return a version number

Set node and npm  

```bash
nvm install v16.13.0
nvm alias default v16.13.0

```
`node -v` and `npm -v` should both return appropriate version numbers.

## Installing AWS Amplify

Create and navigate to the directory you want the bidripper-site loaded into.

`mkdir bidripper && cd bidripper`

Now install the Amplify CLI

`npm install -g @aws-amplify/cli`

## Initializing Bidripper From Git Repository

`amplify init --app https://github.com/Sinux1/bidripper-site.git`  

Amplify will clone into the Bidripper repository and initialize the project locally.  
There will be a prompt:
```
? Select the authentication method you want to use: (Use arrow keys)
❯ AWS profile 
  AWS access keys 
```

When installing the AWS CLI above, a default profile was made. Select 'AWS Profile', then select 'Default'