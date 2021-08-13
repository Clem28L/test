package fr.clem.stateplugin;

import org.bukkit.plugin.java.JavaPlugin;

import fr.clem.stateplugin.commands.commandstate;
import fr.clem.stateplugin.state.State;

public class StatePlugin extends JavaPlugin {
	
	@Override
	public void onEnable() {
		System.out.println("Le StatePlugin viens de s'allumer ! ");
		getCommand("etat").setExecutor(new commandstate());
	}
	
	@Override
	public void onDisable() {
		System.out.println("Le StatePlugin viens de s'eteindre ! ");
	}
	

}
