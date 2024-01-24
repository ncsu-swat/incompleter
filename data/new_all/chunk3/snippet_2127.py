# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62407334/typeerror-missing-1-required-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ingredient = _c_(576395, _a_(576390, _a_(576389, _n_(576388, "Recipe", lambda: Recipe), "Recipe"), "addIngredients"), _n_(576391, "ingredientName", lambda: ingredientName), _n_(576392, "ingredientSize", lambda: ingredientSize), _n_(576393, "ingredientUnitOfMeasure", lambda: ingredientUnitOfMeasure), _n_(576394, "ingredientQuantity", lambda: ingredientQuantity))
_l_(576396)
while _n_(576397, "on", lambda: on):
    _l_(576471)

    menuSelection = _c_(576401, _n_(576398, "int", lambda: int), _c_(576400, _n_(576399, "input", lambda: input), "Would you like to: \n1. Create a recipe\n2. View a recipe\n3. Update a recipe\n4. Delete a recipe\n5. Quit"))
    _l_(576402)
    while _n_(576403, "menuSelection", lambda: menuSelection) != 1 or 2 or 3 or 4 or 5:
        _l_(576470)

        if _n_(576404, "menuSelection", lambda: menuSelection) ==  5:
            _l_(576469)

            on = False
            _l_(576405)
        elif _n_(576406, "menuSelection", lambda: menuSelection) == 1:
            _l_(576468)

            recipeName = _c_(576408, _n_(576407, "input", lambda: input), "Please type in the name of the recipe: ")
            _l_(576409)
            recipeName = _c_(576413, _a_(576411, _n_(576410, "Recipe", lambda: Recipe), "Recipe"), '\n' + _n_(576412, "recipeName", lambda: recipeName))
            _l_(576414)
            addIngredient = True
            _l_(576415)
            while _n_(576416, "addIngredient", lambda: addIngredient):
                _l_(576463)

                ingredientName = _c_(576418, _n_(576417, "input", lambda: input), "Please enter the name of your first ingredient: ")
                _l_(576419)
                ingredientSize = _c_(576421, _n_(576420, "input", lambda: input), "Please enter the size of the ingredient: ")
                _l_(576422)
                ingredientUnitOfMeasure = _c_(576424, _n_(576423, "input", lambda: input), "Please enter the unit of measurement. Grams, millilitres etc:")
                _l_(576425)
                ingredientQuantity = _c_(576427, _n_(576426, "input", lambda: input), "Please enter the quantity of the ingredient:")
                _l_(576428)
                ingredient = ''
                _l_(576429)
                ingredient = _c_(576437, _a_(576432, _a_(576431, _n_(576430, "Recipe", lambda: Recipe), "Recipe"), "addIngredients"), _n_(576433, "ingredientName", lambda: ingredientName), _n_(576434, "ingredientSize", lambda: ingredientSize), _n_(576435, "ingredientUnitOfMeasure", lambda: ingredientUnitOfMeasure), _n_(576436, "ingredientQuantity", lambda: ingredientQuantity))
                _l_(576438)
                continueAdding = True
                _l_(576439)
                answer = _c_(576441, _n_(576440, "input", lambda: input), "Would you like to add another ingredient? Type yes or no.\n")
                _l_(576442)
                while _n_(576443, "continueAdding", lambda: continueAdding):
                    _l_(576459)

                    if _c_(576446, _a_(576445, _n_(576444, "answer", lambda: answer), "lower")) == 'y' or 'yes':
                        _l_(576458)

                        addIngredient = True
                        _l_(576447)
                        break
                        _l_(576448)
                    elif _c_(576451, _a_(576450, _n_(576449, "answer", lambda: answer), "lower")) == 'n' or 'no':
                        _l_(576457)

                        addIngredient = False 
                        _l_(576452) 
                        break  
                        _l_(576453)  
                    else:
                        answer = _c_(576455, _n_(576454, "input", lambda: input), "Please type yes or no.")
                        _l_(576456)
                _c_(576461, _n_(576460, "print", lambda: print), "You have finished adding all of your ingredients.\n")
                _l_(576462)
            _c_(576466, _n_(576464, "print", lambda: print), "You have added " + _n_(576465, "recipeName", lambda: recipeName) + " to the recipe database.")
            _l_(576467)