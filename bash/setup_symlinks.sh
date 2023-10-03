#!/bin/bash

dots_dir="$HOME/development/dotfiles"

home_dir=(
  "wiki"
)

config_dir=(
  "nvim"
#  "i3"
)

shell_config=(
  "bashrc"
  "bashrc.d"
)

for dots in ${home_dir[@]}; do
  ln -sf $dots_dir/$dots $HOME/$dots
  echo "Linked $dots to $HOME/$dots"
done

for dots in ${config_dir[@]}; do
  ln -sf $dots_dir/$dots $HOME/.config/$dots
  echo "Linked $dots to $HOME/.config/$dots"
done

# Modify shell variable for desired shell (bash, fish, zsh, etc.)
for conf in ${shell_config[@]}; do
  shell="bash"
  ln -sf $dots_dir/$shell/$conf $HOME/.$conf
  echo "Linked $shell configurations to $HOME/.$conf"
done
