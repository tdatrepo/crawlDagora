# create file bat to run py scripts

num = 1
string_list = []
for i in range(1, 2801):
    new_string = f'py crawl_dagora2.py {num} {num+50}'
    string_list.append(new_string)
    num += 50
    if i % 560 == 0:
        head = '''
set VENV_PATH=C:\Sources\pyScript\selenium_env\Scripts\\activate
set Deactivate_PATH=C:\Sources\pyScript\selenium_env\Scripts\deactivate
rem Activate the virtual environment
call %VENV_PATH% \n
        '''
        body = '\n'.join(string_list)
        tail = '''
call %Deactivate_PATH%
pause
rem Deactivate the virtual environment
        '''
        all_in_one = head + body + tail
        with open(f'text{i}.bat', 'w') as file:
            file.write(all_in_one)
            string_list.clear()
            # break

# print(f'Strings written to file "{file_path}":\n{string_list}')