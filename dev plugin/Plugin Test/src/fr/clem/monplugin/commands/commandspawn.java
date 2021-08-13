package fr.clem.monplugin.commands;



import org.bukkit.Location;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;



public class commandspawn implements CommandExecutor {

	@Override
	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
		
		if(sender  instanceof Player) {
			Player player = (Player) sender; 
			Location spawn = new Location(player.getWorld(), 218, 64, 87);
			player.sendMessage("teleportation au spawn");
			player.teleport(spawn);
			
		}
		
		return false;
	}

}
