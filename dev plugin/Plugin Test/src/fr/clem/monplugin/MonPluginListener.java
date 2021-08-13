package fr.clem.monplugin;

import java.util.Arrays;

import org.bukkit.Material;
import org.bukkit.enchantments.Enchantment;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.inventory.ItemFlag;
import org.bukkit.inventory.ItemStack;
import org.bukkit.inventory.meta.ItemMeta;

public class MonPluginListener implements Listener {
	
	@EventHandler
	public void onjoin(PlayerJoinEvent event) {
		
		Player player = event.getPlayer();
		player.getInventory().clear();
		player.getInventory().addItem(new ItemStack(Material.IRON_SWORD, 3));
		
		ItemStack customsword = new ItemStack(Material.IRON_SWORD, 1);
		ItemMeta customM  = customsword.getItemMeta();
		customM.setDisplayName("Ma super epée");
		customM.setLore(Arrays.asList("premier ligne", " deuxieme"));
		customM.addEnchant(Enchantment.DAMAGE_ALL, 200, true);
		customM.addItemFlags(ItemFlag.HIDE_ENCHANTS);
		customsword.setItemMeta(customM);
		player.getInventory().setItemInOffHand(customsword);
		

		

		player.updateInventory();
				
		
	}

}
