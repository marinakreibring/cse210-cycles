from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 
class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """
    def __init__(self) -> None:
        super().__init__()
        

# Override the execute(cast, script) method as follows:
    def execute(self, cast, script):
        """Executes the move actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
            """
        # 1) get all the actors from the cast    
        actors = cast.get_all_actors()
        # 2) loop through the actors
        for actor in actors:
            # 3) call the move_next() method on each actor
            actor.move_next()
        
