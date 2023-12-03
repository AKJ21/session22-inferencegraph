from transformers import AutoImageProcessor, AutoModelForImageClassification

def get_processor_and_model(hf_string):
	processor = AutoImageProcessor.from_pretrained(hf_string)
	model = AutoModelForImageClassification.from_pretrained(hf_string)

	return [processor, model]

def save_model_processor(model, processor, save_prefix_str):
	model.save_pretrained(f"./models/{save_prefix_str}/model")
	processor.save_pretrained(f"./models/{save_prefix_str}/processor")

[imagenet_processor, imagenet_model] = get_processor_and_model("google/vit-base-patch16-224")
save_model_processor(imagenet_model, imagenet_processor, "imagenet-vit")

[food_processor, food_model] = get_processor_and_model("nateraw/food")
save_model_processor(food_model, food_processor, "food-classifier")

[cat_processor, cat_model] = get_processor_and_model("dima806/67_cat_breeds_image_detection")
save_model_processor(cat_model, cat_processor, "cat-classifier")

[dog_processor, dog_model] = get_processor_and_model("skyau/dog-breed-classifier-vit")
save_model_processor(dog_model, dog_processor, "dog-classifier")

[vehicle_detection_processor, vehicle_detection_model] = get_processor_and_model("dima806/vehicle_10_types_image_detection")
save_model_processor(vehicle_detection_model,vehicle_detection_processor, "vehicle-classifier")