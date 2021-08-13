package fr.clem.stateplugin.commands;

import java.util.UUID;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

import fr.clem.stateplugin.state.State;

public class commandstate implements CommandExecutor {

	@Override
	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
		// TODO Auto-generated method stub
		
		if(sender instanceof Player) {
			Player player = (Player)sender;
			UUID playeruuid = player.getUniqueId();
			
			
			if(cmd.getName().equalsIgnoreCase("etat") && (args[0].equals("creer"))) {
				if(args.length == 1 ) {
					
					player.sendMessage("la commande est : /etat creer <nomdel'etat>");
					
				}
				
				
				if(args.length >= 2 ) {
					
					String statename = args[1];
				State newstate = new State(statename, player);
				player.sendMessage("§el'état §4["+statename+"]§e a bien été crée");
				
				return true; 
				
				}
				
			}
			
			if(cmd.getName().equalsIgnoreCase("alert")) {
				
			
				
				return true; 
			}
			
		}
		
		return false;
	}




}
