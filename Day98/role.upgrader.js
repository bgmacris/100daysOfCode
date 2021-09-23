var roleUpgrader = {
    run: function(creep) {
	    if(creep.memory.extractEnergy == true && creep.store[RESOURCE_ENERGY] <= 50) {
            //var sources = creep.room.find(FIND_SOURCES);
            var sources = [Game.getObjectById('42c907729fa51ee')];
            if(creep.carry.energy != creep.carryCapacity){
                if(creep.harvest(sources[0]) == ERR_NOT_IN_RANGE || true) {
                    creep.moveTo(sources[0], {visualizePathStyle: {stroke: '#ff00ff'}});
                }
            }else {
                creep.memory.extractEnergy = false;
                creep.say('\u{26A1} build')
            }
        }
        else if(creep.memory.extractEnergy == false){
            if(creep.upgradeController(creep.room.controller) == ERR_NOT_IN_RANGE) {
                creep.moveTo(creep.room.controller, {visualizePathStyle: {stroke: '#ff00ff'}});
            }
            else if(creep.carry.energy == 0){
                creep.memory.extractEnergy = true;
            }
        }
	}
};

module.exports = roleUpgrader;