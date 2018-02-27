*** Settings ***
Library   pylib/SchoolClassLib

*** Test Cases ***
添加班级1-tc000001

    ${ret} =   list_school_class  11113
    log to console   $ret

