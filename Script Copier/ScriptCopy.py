# =============================================================================
# IMPORTING THE LIBRARIES
# =============================================================================

import codecs
import pyperclip
import zlib
from base64 import b64encode
from os import system, listdir, mkdir
from os.path import realpath, dirname
from pyfiglet import Figlet
from rich import print

# =============================================================================
# METHODS FOR VISUALS
# =============================================================================

def print_banner():
  figlet = Figlet(font='big', width=150)
  banner = figlet.renderText(' GODMODE SCRIPT V3')
  print('')
  print(f'[white]{banner}[/white]')

def clear_screen():
  system('cls')

# =============================================================================

def scriptPage():
  script = ('''if defined? MAXIMUM_LEVEL
  MAXIMUMLEVEL = MAXIMUM_LEVEL
end

if defined? BAG_MAX_PER_SLOT
  BAGMAXPERSLOT = BAG_MAX_PER_SLOT
end

def pbChoosePokemonID
  maxNum=PBSpecies.maxValue
  helpText="Input the Pokemon ID from the file named 'PokemonList'"
  Kernel.pbMessage(_INTL("Script added by youtube.com/godmodemaker"))
  sp=ChooseNumberParams.new
  sp.setRange(1, maxNum)
  sp.setInitialValue(1)
  sp.setCancelValue(0)
  output=Kernel.pbMessageChooseNumber(_INTL(helpText),sp)
  return output
end

def pbChooseItemID
  maxNum=PBItems.maxValue
  helpText="Input the Item ID from the file named 'ItemList'"
  Kernel.pbMessage(_INTL("Script added by youtube.com/godmodemaker"))
  sp=ChooseNumberParams.new
  sp.setRange(1, maxNum)
  sp.setInitialValue(1)
  sp.setCancelValue(0)
  output=Kernel.pbMessageChooseNumber(_INTL(helpText),sp)
  return output
end

def pbChooseMoveID
  maxNum=PBMoves.maxValue
  helpText="Input the Move ID from the file named 'MoveList'"
  Kernel.pbMessage(_INTL("Script added by youtube.com/godmodemaker"))
  sp=ChooseNumberParams.new
  sp.setRange(1, maxNum)
  sp.setInitialValue(1)
  sp.setCancelValue(0)
  output=Kernel.pbMessageChooseNumber(_INTL(helpText),sp)
  return output
end

def pbTeleport
  pbFadeOutIn(99999)  {
    $game_variables['''+str(tempArray[1])+''']=$game_map.map_id
    $game_variables['''+str(tempArray[2])+''']=$game_player.x
    $game_variables['''+str(tempArray[3])+''']=$game_player.y
    $game_temp.player_new_map_id='''+mapid+'''
    $game_temp.player_new_x='''+player_loc_x+'''
    $game_temp.player_new_y='''+player_loc_y+'''
    $game_temp.player_new_direction=2
    $scene.transfer_player
    }
  $game_map.refresh
  $game_variables['''+str(tempArray[0])+''']=1
end

def pbTeleportBack
  pbFadeOutIn(99999)  {
    $game_temp.player_new_map_id=$game_variables['''+str(tempArray[1])+''']
    $game_temp.player_new_x=$game_variables['''+str(tempArray[2])+''']
    $game_temp.player_new_y=$game_variables['''+str(tempArray[3])+''']
    $game_temp.player_new_direction=2
    $scene.transfer_player
    }
  $game_map.refresh
  $game_variables['''+str(tempArray[0])+''']=0
end

DEFAULT_FRAME_RATE = Graphics.frame_rate

def pbGodSpeed
  if Graphics.frame_rate==DEFAULT_FRAME_RATE
    Graphics.frame_rate=DEFAULT_FRAME_RATE*4
    Kernel.pbMessage(_INTL("\\\\ts[3] God Speed Enabled \\\\^"))
    return
  else
    Graphics.frame_rate=DEFAULT_FRAME_RATE
    Kernel.pbMessage(_INTL("\\\\ts[1] God Speed Disabled \\\\^"))
    return
  end
end

def pbToggleDebugMode
  if $DEBUG
    $DEBUG = false
    Kernel.pbMessage(_INTL("Debug Mode Deactivated"))
  else
    $DEBUG = true
    Kernel.pbMessage(_INTL("Debug Mode Activated"))
  end
end

def pbInstantPartyHeal
  for i in $Trainer.party
    i.heal
  end
  Kernel.pbMessage(_INTL("All Party Pokemons were Healed!"))
end

def pbNewSelectStyle
  if not File.file?("IDs/trigger.txt")
    file = File.new("IDs/trigger.txt","w")
    file.puts 1 #1 Means Enabled
    file.close
    pbNewListStyle
  else
    trigger = File.read("IDs/trigger.txt").to_i
    if trigger==1
      return true
    else
      return false
    end
  end
end

def pbToggleSelectStyle
  trigger = File.read("IDs/trigger.txt").to_i
  if trigger==1
    file = File.open("IDs/trigger.txt","w")
    file.puts 0
    file.close
    Kernel.pbMessage(_INTL("List Style selected to List Mode"))
  else
    file = File.open("IDs/trigger.txt","w")
    file.puts 1
    file.close
    Kernel.pbMessage(_INTL("List Style selected to ID Mode"))
  end
end

def pbAddStorageBoxes
  helpText="Enter the number of Pokemon Storage Boxes you need"
  sp=ChooseNumberParams.new
  sp.setRange(1, 99)
  sp.setInitialValue(1)
  sp.setCancelValue(0)
  n=Kernel.pbMessageChooseNumber(_INTL(helpText),sp)
  $PokemonStorage.addBox(n)
end

def pbGetAllPokemonLevel
  helpText="What level do you want them to be?"
  sp=ChooseNumberParams.new
  sp.setRange(1, MAXIMUMLEVEL)
  sp.setInitialValue(1)
  sp.setCancelValue(0)
  n=Kernel.pbMessageChooseNumber(_INTL(helpText),sp)
  return n
end

def pbGetAllPokemon
  level=pbGetAllPokemonLevel
  for i in 1...PBSpecies.maxValue+1
    begin
      a = getConstantName(PBSpecies,i)
    rescue
      a = ""
    end
    if a != ""
      begin
        pbAddPokemonSilent i,level
      end
    end
  end
end''')
  pyperclip.copy(script)
  print("\[i] Copied\n")

# =============================================================================

def pauseMenu():
  print("[+] Pause Menu Choices:")
  print("   [1] Initializing new Options")
  print("   [2] Adding Menu Options")
  print("   [3] Menu Option Action")
  print("   [0] Exit 'Pause Menu Scripts'\n")
  option = input("Your Choice: ")
  print("\n")
  if option.isnumeric():
    if option == '1':
      initialize()
      pauseMenu()
    elif option == '2':
      add_menu()
      pauseMenu()
    elif option == '3':
      action()
      pauseMenu()
    elif option == '0':
      print("\[i] Exiting Pause Menu Choices...\n")
    else:
      print("[!] Invalid Input: Entered value must be between 0 & 3 only")
      pauseMenu()
  else:
    print("[!] Invalid Input: Entered value must be an Integer\n")
    pauseMenu()

def initialize():
  pyperclip.copy('''cmdTeleport=-1\n\t\tcmdTeleportBack=-1''')
  print("\[i] Copied\n")

def add_menu():
  pyperclip.copy('''if $game_variables['''+str(checkVariable)+''']==0
      commands[cmdTeleport=commands.length]=_INTL("Teleport")
    else
      commands[cmdTeleportBack=commands.length]=_INTL("Teleport Back")
    end''')
  print("\[i] Copied\n")

def action():
  pyperclip.copy('''elsif cmdTeleport>=0 && command==cmdTeleport
        pbTeleport
        break
      elsif cmdTeleportBack>=0 && command==cmdTeleportBack
        pbTeleportBack
        break''')
  print("\[i] Copied\n")

# =============================================================================

def controls():
  print("[+] Control Choices:")
  print("   [1] Key Press Action")
  print("   [2] Add F10 and F11 Keys")
  print("   [0] Exit Control Choices\n")
  option = input("Your Choice: ")
  print("\n")
  if option.isnumeric():
    if option == '1':
      control_action()
      controls()
    elif option == '2':
      print("\[i] Go to Key Initializing script page (Usually, PokemonControls) to add the keys!")
      addNewKeys()
      controls()
    elif option == '0':
      print("\[i] Exiting Control Choices Menu...\n")
    else:
      print("[!] Invalid Input: Value must only be 0,1, or 2\n")
      controls()
  else:
    print("[!] Invalid Input: Entered value must be Integer\n")
    controls()

def control_action():
  pyperclip.copy('''if trigger?(Input::F7)
      pbToggleDebugMode
    end
    if trigger?(Input::ALT)
      pbGodSpeed
    end
    if trigger?(Input::F6)
      if $game_variables['''+str(checkVariable)+''']==0
        pbTeleport
      elsif $game_variables['''+str(checkVariable)+''']==1
        pbTeleportBack
      end
    end
    if trigger?(Input::F10)
      pbInstantPartyHeal
    end
    if trigger?(Input::F11)
      pbToggleSelectStyle
    end''')
  print("\[i] Copied\n")

def addNewKeys():
  print("\[i] Paste the Copied Text after the last Initialization in 'module Input'")
  pyperclip.copy(f"F10 = {lastValue+1}\n  F11 = {lastValue+2}")
  input("[=] Press Enter when you are done...")
  print("\[i] In 'def self.buttonToKey(button) > case button', add the copied text under the last Initialization.\n")
  pyperclip.copy("when Input::F10\n        return [0x79]\n      when Input::F11\n        return [0x7A]")

# =============================================================================

def splitter():
  pyperclip.copy("#====================================[ GMM ]====================================")
  print("\[i] Copied\n")

# =============================================================================

def pbsExtractor():
  print("\[i] Copied\n")
  pyperclip.copy('''def pbExtractPBS
  directory_name = "IDs"
  Dir.mkdir(directory_name) unless File.exists?(directory_name)
  pbExtractSpeciesList
  pbExtractItemList
  pbExtractMoveList
  pbMakeTrigger
end

def pbExtractSpeciesList
  file = File.new("IDs/PokemonList.txt", "w")
  maxLength = PBSpecies.maxValue.to_s.length
  for i in 1..PBSpecies.maxValue
    begin
      pname = getConstantName(PBSpecies,i)
    rescue
      pname = "Undefined"
    end
    iLength = i.to_s.length
    zero = "0" * (maxLength - iLength)
    output = zero + i.to_s + " " + pname
    file.puts output
  end
  file.close
  Kernel.pbMessage(_INTL("Species List Genereted"))
end

def pbExtractItemList
  file = File.new("IDs/ItemsList.txt", "w")
  maxLength = PBItems.maxValue.to_s.length
  for i in 1..PBItems.maxValue
    begin
      iname = getConstantName(PBItems,i)
    rescue
      iname = "Undefined"
    end
    iLength = i.to_s.length
    zero = "0" * (maxLength - iLength)
    output = zero + i.to_s + " " + iname
    file.puts output
  end
  file.close
  Kernel.pbMessage(_INTL("Items List Genereted"))
end

def pbExtractMoveList
  file = File.new("IDs/MoveList.txt", "w")
  maxLength = PBMoves.maxValue.to_s.length
  for i in 1..PBMoves.maxValue
    begin
      mname = getConstantName(PBMoves,i)
    rescue
      mname = "Undefined"
    end
    iLength = i.to_s.length
    zero = "0" * (maxLength - iLength)
    output = zero + i.to_s + " " + mname
    file.puts output
  end
  file.close
  Kernel.pbMessage(_INTL("Moves List Genereted"))
end

def pbMakeTrigger
  file = File.open("IDs/trigger.txt","w")
  file.puts 1
  file.close
  Kernel.pbMessage(_INTL("Trigger File Created"))
end''')

# =============================================================================

def catchTrainerPokemon():
  print("\[i] Go to the PokeBattle_Battle script page")
  print("\[i] Find 'if @opponent && (!pbIsSnagBall?(ball) || !battler.isShadow?)'")
  pyperclip.copy("if @opponent && !Input.trigger?(Input::CTRL)")
  print("\[i] And then replace the line with the copied text...\n")

# =============================================================================

def addStorageBox():
  print("\[i] Go to PokemonStorage > class PokemonStorage")
  print("\[i] Add the copied function to the class")
  print("\[i] Add a new event that uses the function")
  pyperclip.copy('''def addBox(n=1)
    for i in 1..n
      @boxes.push(PokemonBox.new(_ISPRINTF("Box " + (maxBoxes+1).to_s), maxPokemon(0)))
    end
  end''')

# =============================================================================

def main(nineteen_plus=False):
  if nineteen_plus:
    main_new()
  print("[+] Available Options:")
  print("   [1] Scripts Page")
  print("   [2] Pause Menu Codes")
  print("   [3] Control Codes")
  print("   [4] Splitter Text")
  print("   [5] PBS Extract Page")
  print("   [6] Catch Trainer Pokemon")
  print("   [7] Add Storage Boxes")
  print("   [8] Clear Input Screen")
  print("   [0] Exit Input Mode\n")
  choice = input("Your Choice: ")
  print('')
  if choice.isnumeric():
    if choice == '0': # Exit
      print("\n\[i] Stopped Input Mode...\n\n[!] Exiting Program\n")
    elif choice == '1':
      scriptPage()
      main()
    elif choice == '2':
      pauseMenu()
      main()
    elif choice == '3':
      controls()
      main()
    elif choice == '4':
      splitter()
      main()
    elif choice == '5':
      pbsExtractor()
      main()
    elif choice == '6':
      catchTrainerPokemon()
      main()
    elif choice == '7':
      addStorageBox()
      main()
    elif choice == '8':
      clear_screen()
      print_banner()
      main()
    else:
      print("\n[!] Invalid Input: Only values between 0 & 8 Allowed\n")
      main()
  else:
    print("\n[!] Invalid Input: The Input must be an Integer")
    main()

# =============================================================================

def create_god_mode_plugin():
  plugins_path = input("[=] Enter Path to Plugins Folder: ") + "\\God Mode"
  print("")
  mkdir(plugins_path)
  scripts_path = f"{script_directory}\\Scripts\\v19+\\Plugins"
  script_list = listdir(scripts_path)
  for script in script_list:
    with open(f"{scripts_path}\\{script}", "r") as f:
      data = variables_to_values(f.read())
    script_file_name = script
    if script != "meta.txt":
      script_file_name = script.replace(".txt", ".rb")
    with open(f"{plugins_path}\\" + script_file_name, 'w') as f:
      f.write(data)
  print("[!] [green]Created Plugins Scripts in Given Directory.[/green]\n")

# =============================================================================

def open_script_new(script):
  script_list = {
    '2': 'Catch_Trainer_Pokemon.txt',
    '3': 'Choose_Move.txt',
    '4': 'Choose_Pokemon_Species.txt',
    '5': 'Debug_Add_Item.txt',
    '6': 'Debug_God_Mode.txt',
    '7': 'Menu_Teleport.txt'
  }
  path_nineteen = "./Scripts/v19+/"
  with open(path_nineteen + script_list[script], 'r') as f:
    return f.read()

def variables_to_values(data):
  VAR_CHECK = checkVariable
  VAR_MAP_ID_OLD, VAR_PLAYER_X, VAR_PLAYER_Y = range(
    checkVariable + 1, checkVariable + 4
  )
  MAP_ID_NEW = mapid
  PLAYER_X_NEW, PLAYER_Y_NEW = player_loc_x, player_loc_y
  val_list = [
    VAR_CHECK, VAR_MAP_ID_OLD, VAR_PLAYER_X, VAR_PLAYER_Y, MAP_ID_NEW,
    PLAYER_X_NEW, PLAYER_Y_NEW
  ]
  var_list = [
    "{VAR_CHECK}", "{VAR_MAP_ID_OLD}", "{VAR_PLAYER_X}", "{VAR_PLAYER_Y}",
    "{MAP_ID_NEW}", "{PLAYER_X_NEW}", "{PLAYER_Y_NEW}"
  ]
  for i in range(len(var_list)):
    data = data.replace(var_list[i], str(val_list[i]))
  return data

# =============================================================================

def main_new():
  print("[+] Available Options:")
  print("   [1] Create God Mode Plugin")
  print("   [2] Catch Trainer Pokemon")
  print("   [3] Choose Move Modification")
  print("   [4] Choose Pokemon Modification")
  print("   [5] Debug: Add Items Modification")
  print("   [6] Debug: God Mode Scripts")
  print("   [7] Pause Menu Modification")
  print("   [8] Clear Screen")
  print("   [0] Exit Script\n")
  choice = input("Your Choice: ")
  print('')
  data_copy = lambda c: pyperclip.copy(variables_to_values(open_script_new(c)))
  if choice == '0':
    print("\n\[i] Stopped Input Mode...\n\n[!] Exiting Program\n")
  elif choice == '1':
    create_god_mode_plugin()
    main_new()
  elif choice == '2':
    data_copy(choice)
    print("[!] Script Name: [i]Battle_CatchAndStoreMixin[/i]")
    print("    Search Term: [green]!(GameData::Item.get(ball).is_snag_ball?[/green]")
    print("    Instruction: Add copied line before Search Term, indent & end.")
    print("")
    main_new()
  elif choice == '3':
    data_copy(choice)
    print("[!] Script Name: [i]Editor_Utilities[/i]")
    print("    Search Term: [green]def pbChooseMoveList(default = nil)[/green]")
    print("    Instruction: Replace the function with the copied function.")
    print("")
    main_new()
  elif choice == '4':
    data_copy(choice)
    print("[!] Script Name: [i]Editor_Utilities[/i]")
    print("    Search Term: [green]def pbChooseSpeciesList(default = nil)[/green]")
    print("    Instruction: Replace the function with the copied function.")
    print("")
    main_new()
  elif choice == '5':
    data_copy(choice)
    print("[!] Script Name: [i]Debug_MenuCommands[/i]")
    print("    Search Term: [green]MenuHandlers.add(:debug_menu, :add_item, {[/green]")
    print("    Instruction: Replace the whole MenuHandler with the copied one.")
    print("")
    main_new()
  elif choice == '6':
    data_copy(choice)
    print("[!] Script Name: [i]Debug_MenuCommands[/i]")
    print("    Search Term: None")
    print("    Instruction: Add the copied text to the bottom of the Script.")
    print("")
    main_new()
  elif choice == '7':
    data_copy(choice)
    print("[!] Script Name: [i]UI_PauseMenu[/i]")
    print("    Search Term: [green]MenuHandlers.add(:pause_menu, :debug, {[/green]")
    print("    Instruction: Paste the copied text after the Searched MenuHandler.")
    print("")
    main_new()
  elif choice == '8':
    clear_screen()
    print_banner()
    main_new()
  else:
    print("\n[!] Invalid Input: Only values between 0 & 8 Allowed\n")
    main_new()

# =============================================================================

if __name__ == "__main__":
  print_banner()
  print("\[i] Made by: Ishaan Pathak\n")
  print("\[i] Starting Input Mode...\n")

  # Checking if Game is v19 Above. True means the game is v19+
  version_nineteen_plus = input(
    "\n[=] Is the game using Essentials v19 or Above? [y/N]: "
  ).lower() == 'y'

  script_directory = realpath(dirname(__file__))
  
  checkVariable = int(input("[=] Enter the Check Variable: "))
  tempArray = range(checkVariable, checkVariable+4)
  mapid = str(int(input("[=] Enter the MapID: ")))
  player_loc_x = str(int(input("[=] Enter Player X Coordinate: ")))
  player_loc_y = str(int(input("[=] Enter Player Y Coordinate: ")))
  if not version_nineteen_plus:
    lastValue = int(
      input("[=] Enter the last initialized value in 'module Input': ")
    )
  
  print("\n\[i] Successfully received all data, starting main program...\n")
  main() if not version_nineteen_plus else main_new()