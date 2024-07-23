from Make_Database import print_info_users,print_info_servers

def test_print_info_users():
    assert print_info_users()
    assert print_info_users()[0].player_name=="Peta"
    assert str(print_info_users()[3].player_money)=="0"
    assert str(print_info_users()[5].player_is_online)=="True"
    
def test_print_info_servers():
    assert print_info_servers()
    assert str(print_info_servers()[0].server_name)=="Minecraft"
    assert str(print_info_servers()[2].server_start)=="24.04.2018"
    assert str(print_info_servers()[1].server_is_alive)=="True"
