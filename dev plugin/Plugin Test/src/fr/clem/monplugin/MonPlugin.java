package fr.clem.monplugin;

import org.bukkit.plugin.java.JavaPlugin;

import fr.clem.monplugin.commands.Commandtest;
import fr.clem.monplugin.commands.commandspawn;



public class MonPlugin extends JavaPlugin {
	
	@Override
	public void onEnable() {
		System.out.println("Le Plugin viens de s'allumer ! ");
		getCommand("test").setExecutor(new Commandtest());
		getCommand("alert").setExecutor(new Commandtest());
		getCommand("spawn").setExecutor(new commandspawn());
		getServer().getPluginManager().registerEvents(new MonPluginListener() , this);
		
	}
	
	@Override
	public void onDisable() {
		System.out.println("Le Plugin viens de s'eteindre ! ");
	}


}
