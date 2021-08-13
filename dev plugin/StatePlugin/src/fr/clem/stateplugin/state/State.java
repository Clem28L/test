package fr.clem.stateplugin.state;

import java.util.ArrayList;

import org.bukkit.entity.Player;



public class State {
	
	private String name_of_state ;
	private Player manager ;
	private ArrayList<Player> members = new ArrayList<>();
	
	public State(String name_of_state, Player manager) {
		// TODO Auto-generated constructor stub
		this.setName_of_state(name_of_state);
		this.setManager(manager); 
		this.members.add(manager);
		
	}

	public String getName_of_state() {
		return name_of_state;
	}

	public void setName_of_state(String name_of_state) {
		this.name_of_state = name_of_state;
	}

	public Player getManager() {
		return manager;
	}

	public void setManager(Player manager) {
		this.manager = manager;
	}


	
}
