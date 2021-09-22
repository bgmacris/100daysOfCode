var roleHarvester = {
    run: function(creep) {
        if(creep.store.getFreeCapacity() > 0){
            var sources = creep.room.find(FIND_SOURCES);
            if(creep.harvest(sources[0]) == ERR_NOT_IN_RANGE){
                creep.moveTo(sources);
            }else{
                console.log("No")
            }
        }
        else if(Game.spawns['root'].energy < Game.spawns['root'].energyCapacity){
            if(creep.transfer(Game.spawns['root'], RESOURCE_ENERGY) == ERR_NOT_IN_RANGE){
                creep.moveTo(Game.spawns['root']);
            }
        }
    }
}

module.exports = roleHarvester;