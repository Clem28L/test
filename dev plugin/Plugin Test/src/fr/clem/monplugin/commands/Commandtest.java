package fr.clem.monplugin.commands;

import org.bukkit.Bukkit;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

public class Commandtest implements CommandExecutor {

	@Override
	public boolean onCommand(CommandSender sender, Command cmd, String msg, String[] args) {
		// TODO Auto-generated method stub
		
		if(sender instanceof Player) {
			Player player = (Player)sender; 
			
			if(cmd.getName().equalsIgnoreCase("test")) {
				player.sendMessage("�ebravo tu as reusit le �9test ");
				return true; 
			}
			
			if(cmd.getName().equalsIgnoreCase("alert")) {
				
				if(args.length == 0 )
					player.sendMessage("la commande est : /alert <message>");
				
				if(args.length >= 1 ) {
					
					StringBuilder bc = new StringBuilder();
					for(String part : args) {
						bc.append(part + " ");
					}
					Bukkit.broadcastMessage("["+player.getName() + "]"+ bc.toString());
				}
				
				
				
				return true; 
			}
			
		}
		

		return false;
	}

}
