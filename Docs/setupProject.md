# Setting up for developers

## Required packages

Some basics just in case (curl and git are the most important)

`sudo apt update -y && sudo apt upgrade -y && sudo apt autoremove && sudo apt install curl gcc make perl git -y`  

### Make sure AWS CLI v2 is installed

Navigate to where you want to download the install package for aws cli v2 and run  

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
source ~/.bashrc
```

### Configure AWS profile

Have your (secret) access keys ready and then run 

`aws configure`

Follow the questions. When asked enter `us-west-2` for region, and `json` for the question about return data types. This will configure a *_default_* profile that will be used later when pulling the amplify project.

### Now for nvm, npm, and node

From whatever directory  you installed aws cli, run

`curl -sL https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.0/install.sh -o install_nvm.sh | bash install_nvm.sh`

You can close and reopen your terminal like an amateur for this to take effect or run  

```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
```

Sanity Check
`nvm --version` should return a version number

Install and set latest versions of node and npm  

```bash
nvm install --lts
nvm alias default lts/fermium
```
`node -v` and `npm -v` should both return version numbers.

## Clone repo

You should already have access by way of ssh key

`git clone git@bitbucket.org:smazarei/capstone.git`

### Install node_modules

Since the repo gitignores node_modules, but tracks packages, to install the appropriate packages run  

`npm install`

There will be some warnings, run `nmp audit fix` to take care of the ones that aren't breaking.  

### Install Amplify

`npm add -g aws-amplify @aws-amplify/ui-react @aws-amplify/cli`



