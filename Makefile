get_models:
	mkdir -p models
	curl -o ./model.zip https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
	unzip model.zip -d models
	mv models/vosk-model-small-en-us-0.15 models/en
	rm model.zip
	
	curl -o ./model.zip https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip
	unzip model.zip -d models
	mv models/vosk-model-small-ru-0.22 models/ru
	rm model.zip
