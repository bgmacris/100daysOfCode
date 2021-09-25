var roleUpgrader = {
    run: function (creep) {
        if (creep.memory.working == true && creep.store[RESOURCE_ENERGY] <= 50) {
            var sources = Game.getObjectById(creep.memory.sourceID);
            if (creep.carry.energy != creep.carryCapacity) {
                if (creep.harvest(sources) == ERR_NOT_IN_RANGE || true) {
                    creep.moveTo(sources, { visualizePathStyle: { stroke: '#ff00ff' } });
                }
            } else {
                creep.memory.working = false;
                creep.say('\u{26A1} build')
            }
        }
        else if (creep.memory.working == false) {
            if (creep.upgradeController(creep.room.controller) == ERR_NOT_IN_RANGE) {
                creep.moveTo(creep.room.controller, { visualizePathStyle: { stroke: '#ff00ff' } });
            }
            else if (creep.carry.energy == 0) {
                creep.memory.working = true;
            }
        }
    }
};

module.exports = roleUpgrader;