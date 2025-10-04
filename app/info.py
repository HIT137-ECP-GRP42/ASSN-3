
def oop_explanations():
    """
    OOP ideas applied:

     Multiple inheritance: To combine (logging and theming) behaviors, AppGUI is built on top of LoggingMixin and themeMixin.
       without using the same code twice.

     Multiple decorators: UI actions are timed, logged, and audited using two decorators (ui_action and audit decorators) that act without changing their bodies.

     Encapsulation: Model objects with a straightforward run(...) interface—a GUI state—are the basis for classes.
       Widgets and handlers are a part of AppGUI methods.

     Polymorphism: Depending on the task selected, a single call site (run inference) can send out to different behaviors.
       (image classification vs. text generation), but both offer run().

     Method overriding: Subclasses, such as TextGenerationModel and ImageClassificationModel, carry out their own tasks.
       base initializer and provide their run() implementations.
     Separation of concern (model vs. GUI) Clean (minimal surface area), Separation of concern Minimal surface area for user actions, Clean Separation of concerns (model vs. GUI)
       particular browse/run/clear handlers to preserve the predictability of the flow.


    """
    return oop_explanations.__doc__.strip()


def model_brief(text_model, image_model):
    """
    Text generation: sshleifer/tiny-gpt2, a small version of GPT-2 for quick CPU text-gen demonstrations.
    Image classification: apple/mobilevit-xx-small, an apple low-power MobileViT version for image classification labels in the ImageNet-1k style.
    """
    txt = model_brief.__doc__.strip()
    return txt