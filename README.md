yaml_env
=============
Generates Bash profile variables from YAML input

# Example / Output  
    $ python yaml.env.py input.yml
    --- Gives ---
    export OH_MY_SO_MANY_KEYS="yet_another_value"
    export ANOTHER_KEY="another_value"
    export LAST_KEY="last_value"
    export KEY="value"

# Add to Bash Profile  
    $ python yaml.env.py input.yml >> ~/.bash_profile
