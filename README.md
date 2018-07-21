# Chatbots - Eine Einführung 2018
Hier sind Ressources zu meinem Kurzvortrag zu Chatbots bei [Hack to the future in Friedrichshafen](https://www.hacktothefuture.de/de/startseite/httf-friedrichshafen/). Um die Präsentation anzuschauen, starte [PITCHME.md bei GitPitch](https://gitpitch.com/data-henrik/chatbot-talk2018/deutsch_httf).

![](assets/images/can-chat-chatting-362.jpg)

# Überblick
[Wikipedia beschreibt Chatbots](https://de.wikipedia.org/wiki/Chatbot) wie folgt:
> Ein Chatterbot, Chatbot oder kurz Bot ist ein textbasiertes Dialogsystem, welches das Chatten mit einem technischen System erlaubt. Er hat je einen Bereich zur Textein- und -ausgabe, über die sich in natürlicher Sprache mit dem dahinterstehenden System kommunizieren lässt.

Chatbots haben zwei Hauptaufgaben:   
> Die Benutzerabsicht erkennen und eine dazu passende Antwort erzeugen.

Im Zusammenhang mit Chatbots gibt es die folgenden Konzepte.
* **Intents** (Absichten) sind die Ziele bzw. erwünschte Ergebnisse der Interaktion. Das kann z.B. der aktuelle Wetterbericht, ein Witz oder das Tagesprogramm sein.
* **Entities** (Dinge oder Entitäten) sind Objekte jeder Art. Dies kann ein Ort für einen Wetterbericht, das Datum, Personen, Produkte usw. sein. Sie können auch umschrieben werden, z.B. "heute" oder "morgen", "dieser Nachmittag".
* Der **Dialog** oder Dialogbaum / Dialogfluss beschreibt die Struktur bei der Interaktion zwischen Bot und Nutzer. Diese kann u.a. sehr komplex sein, wenn ein Gespräch ähnlich wie bei Mensch zu Mensch gewünscht ist.   
* **Slots** oder auch Aussparung oder Schlitz wird von Chatbot-Systemen zum Sammeln von Eingaben verwendet. Jeder Slot beschreibt eine erwartete Benutzereingabe. Für einen Wetterbericht wird der Ort und das Datum benötigt.   
* Der **Context** bzw. Kontext beschreibt die Statusinformationen bzw. Daten, die von einem Schritt der Interaktion zum nächsten Schritt transportiert werden. Das können alle aktuellen Eingaben (aus den Slots), der aktuelle Knoten im Dialogbaum und der aktuelle "Intent" sind.

# Ressources
Die folgenden Komponenten habe ich verwendet:
* [Botkit](https://github.com/howdyai/botkit/)
* [Botkit Middleware für IBM Watson Assistant (Conversation)](https://github.com/watson-developer-cloud/botkit-middleware)
* [IBM Watson Assistant service](https://console.bluemix.net/docs/services/conversation/index.html#about)
Die gesamte Kombination lässt sich kostenlos betreiben.

Weitere Informationen lassen sich im englischsprachigen ["master branch"](https://github.com/data-henrik/chatbot-talk2018) finden.
