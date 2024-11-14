function pocionMagica(potions, target){
    const seen = {}

    for (let i = 0; i < potions.length; i++){
        const currentPotion = potions[i]
        const complement = target - currentPotion

        if(seen[complement] !== undefined){
            return [seen[complement], i]
        }
        seen[currentPotion] = i
    }
}

const potions = [4, 5, 6, 2]
const goal = 8

createMagicPotion(potions, goal) // [2, 3]