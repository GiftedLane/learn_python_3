# DevNet: Bash & Git Commands List

This is a list of the different commands I use when working with Git and Bash. A more complete list can be found here https://www.educative.io/blog/bash-shell-command-cheat-sheet.

## Bash commands

```bash
#Customize the Bash prompt
PS1='\W\$ '
```

```bash
#Clear all the lines in terminal for a fresh window
clear
```

```bash
#Access the Help Manual
man
```

```bash
#Change directory
cd /some folder/some_sub_folder
```

```bash
#List files in the current directory
ls
```

```bash
#Print working directory
pwd
```

```bash
#Copy & paste a file
cp source_file.txt destination_file.txt
```

```bash
#Create a new file
touch text_file.txt
```

```bash
#Replace ALL the text in the file with new text
echo "some text" > text_file.txt 

#Add text to the end of the file, without erasing the existing text
echo "some text" >> text_file.txt 
```

```bash
#Create a new directory
mkdir newDirectory
```

## Git commands

```bash
#Tell Git to initialize the current directory
git init

#Tell Git to create & initialize a new directory
git init dir/sub_dir
```

```bash
#View commit history
git log
```

```bash
#Check status of changes to repo
#Check if local branch is ahead/behind remote repo
git status
```

```bash
#Stage specific file for commit
git add text_file.txt

#Stage ALL files for commit
git add .
```

```bash
#Commit changes
git commit
```

```bash
#See changes to the remote repo before pulling them in
git fetch --dry-run
```

## Acknowledgments

Animal Crossing New Horizons was played heavily during study breaks.
