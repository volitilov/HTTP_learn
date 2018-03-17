status code ::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Код состояния является частью первой строки ответа сервера. Он 
# представляет собой целое число из трёх цифр. Первая цифра 
# указывает на класс состояния. За кодом ответа обычно следует 
# отделённая пробелом поясняющая фраза на английском языке, 
# которая разъясняет человеку причину именно такого ответа.
# Клиент узнаёт по коду ответа о результатах его запроса и 
# определяет, какие действия ему предпринимать дальше. Набор 
# кодов состояния является стандартом, и они описаны в 
# соответствующих документах RFC. Введение новых кодов должно 
# производиться только после согласования с IETF. Клиент может 
# не знать все коды состояния, но он обязан отреагировать в 
# соответствии с классом кода.

# В настоящее время выделено пять классов кодов состояния.

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
1xx Информационный (informational)
# Информирование о процессе передачи. В HTTP/1.0 — сообщения с 
# такими кодами должны игнорироваться.
# В HTTP/1.1 — клиент должен быть готов принять этот класс 
# сообщений как обычный ответ, но ничего отправлять серверу не 
# нужно.
# Сами сообщения от сервера содержат только стартовую строку 
# ответа и, если требуется, несколько специфичных для ответа 
# полей заголовка. Прокси-серверы подобные сообщения должны 
# отправлять дальше от сервера к клиенту.

100 Continue
# Этот промежуточный ответ указывает, что все до сих пор в порядке 
# и что клиент должен продолжить запрос или проигнорировать его, 
# если он уже завершен.

101 Switching Protocol
# Этот код отправляется в ответ на заголовок запроса обновления 
# клиентом и указывает протокол, который переключает сервер.

102 Processing
# Этот код указывает, что сервер получил и обрабатывает запрос, 
# но ответа пока нет.




# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
2xx Успех (Success)
# Информирование о случаях успешного принятия и обработки запроса 
# клиента. В зависимости от статуса, сервер может ещё передать 
# заголовки и тело сообщения.

200 OK
# Успешный запрос. Значение успеха зависит от метода HTTP: 
# GET: ресурс был извлечен и передан в теле сообщения. 
# HEAD: заголовки объектов находятся в теле сообщения. 
# PUT или POST: ресурс, описывающий результат действия, 
# передается в теле сообщения. 
# TRACE: Тело сообщения содержит сообщение запроса, полученное 
# сервером

201 Created
# Запрос преуспел, и в результате был создан новый ресурс. Обычно 
# это ответ, отправленный после запроса POST, или после некоторых 
# запросов PUT.

202 Accepted
# Запрос был получен, но еще не принят. Это не является 
# обязательным, что означает, что в HTTP нет способа отправить 
# асинхронный ответ, указывающий на результат обработки запроса. 
# Он предназначен для случаев, когда другой процесс или сервер 
# обрабатывает запрос или для пакетной обработки.

203 Non-Authoritative Information
# Этот код ответа означает, что возвращаемый набор метаданных не 
# является точным, установленным на сервере происхождения, но 
# собранным из локальной или сторонней копии. За исключением этого 
# условия, 200 OK ответ должен быть предпочтительным вместо этого 
# ответа.

204 No Content
# Для этого запроса нет контента, но заголовки могут быть полезны. 
# Пользовательский агент может обновить свои кэшированные заголовки 
# для этого ресурса новыми.

205 Reset Content
# Этот код ответа отправляется после выполнения запроса, чтобы 
# сообщить пользователю об отзыве документа агента, который 
# отправил этот запрос.

206 Partial Content
# Этот код ответа используется из-за заголовка диапазона, 
# отправленного клиентом для разделения загрузки на несколько 
# потоков.

207 Multi-Status
# Ответ Multi-Status передает информацию о нескольких ресурсах в 
# ситуациях, когда может потребоваться несколько кодов состояния.

208 Multi-Status
# Используется внутри элемента ответа DAV: propstat, чтобы 
# избежать повторного перечисления внутренних элементов 
# нескольких привязок к одной и той же коллекции.

226 IM Used
# Сервер выполнил запрос GET для ресурса, и ответ представляет 
# собой представление результата одного или нескольких манипуляций 
# с экземплярами, применяемых к текущему экземпляру.



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
3xx Перенаправление (Redirection)
# Сообщает клиенту, что для успешного выполнения операции 
# необходимо сделать другой запрос (как правило по другому URI). 
# Из данного класса пять кодов 301, 302, 303, 305 и 307 относятся 
# непосредственно к перенаправлениям (редирект). Адрес, по 
# которому клиенту следует произвести запрос, сервер указывает 
# в заголовке Location. При этом допускается использование 
# фрагментов в целевом URI.

300 Multiple Choice
# Запрос имеет более одного возможного ответа. Пользователь-агент 
# или пользователь должны выбрать один из них. Не существует 
# стандартизированного способа выбора одного из ответов.

301 Moved Permanently
# Этот код ответа означает, что URI запрашиваемого ресурса был 
# изменен. Возможно, в ответе будет указан новый URI.

302 Found
# Этот код ответа означает, что URI запрашиваемого ресурса 
# временно изменен. Новые изменения в URI могут быть сделаны в 
# будущем. Поэтому этот же URI должен использоваться клиентом в 
# будущих запросах.

303 See Other
# Сервер отправил этот ответ, чтобы направить клиента для 
# получения запрошенного ресурса в другом URI с запросом GET.

304 Not Modified
# Это используется для кеширования. Он сообщает клиенту, что 
# ответ не был изменен, поэтому клиент может продолжать 
# использовать ту же кешированную версию ответа.

305 Use Proxy
# Был определен в предыдущей версии спецификации HTTP, чтобы 
# указать, что запрошенный ответ должен быть доступен прокси. 
# Он устарел из-за проблем с безопасностью в отношении 
# конфигурации прокси-сервера в зоне.

306 unused
# Этот код ответа больше не используется, он просто 
# зарезервирован в настоящее время. Он использовался в 
# предыдущей версии спецификации HTTP 1.1.

307 Temporary Redirect
# Сервер отправляет этот ответ, чтобы направить клиента на 
# получение запрошенного ресурса в другом URI с помощью того 
# же метода, который использовался в предыдущем запросе. Это 
# имеет ту же семантику, что и код ответа HTTP 302 Found, за 
# исключением того, что пользовательский агент не должен 
# изменять используемый HTTP-метод: если в первом запросе 
# использовался POST, во втором запросе должен использоваться 
# POST.

308 Permanent Redirect
# Это означает, что ресурс теперь постоянно находится в другом 
# URI, указанном заголовком Location: HTTP Response. Это имеет 
# ту же семантику, что и код ответа 301 Moved Permently HTTP, 
# за исключением того, что пользовательский агент не должен 
# изменять используемый HTTP-метод: если в первом запросе 
# использовался POST, во втором запросе должен использоваться 
# POST.



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
4xx Ошибка клиента (Client Error)
# Указание ошибок со стороны клиента. При использовании всех 
# методов, кроме HEAD, сервер должен вернуть в теле сообщения 
# гипертекстовое пояснение для пользователя.

400 Bad Request
# Этот ответ означает, что сервер не смог понять запрос из-за 
# недействительного синтаксиса.

401 Unauthorized
# Хотя стандарт HTTP указывает «неавторизованный», семантически 
# этот ответ означает «unauthenticated». То есть клиент должен 
# аутентифицироваться, чтобы получить запрошенный ответ.

402 Payment Required
# Этот код ответа зарезервирован для будущего использования. 
# Первоначальная цель создания этого кода заключалась в 
# использовании его для цифровых платежных систем, однако в 
# настоящее время это не используется.

403 Forbidden
# Клиент не имеет прав доступа к контенту, то есть они 
# неавторизированы, поэтому сервер отказывается дать правильный 
# ответ. В отличие от 401, идентификатор клиента известен 
# серверу.

404 Not Found
# Сервер не может найти запрошенный ресурс. В браузере это 
# означает, что URL-адрес не распознается. В API это также 
# означает, что конечная точка действительна, но сам ресурс не 
# существует. Серверы могут также отправить этот ответ вместо 
# 403, чтобы скрыть существование ресурса от неавторизованного 
# клиента. Этот код ответа, вероятно, самый известный из-за его 
# частого появления в Интернете.

405 Method Not Allowed
# Метод запроса известен серверу, но был отключен и не может 
# быть использован. Например, API может запретить УДАЛЕНИЕ 
# ресурса. Два обязательных метода GET и HEAD никогда не должны 
# быть отключены и не должны возвращать этот код ошибки.

406 Not Acceptable
# Этот ответ отправляется, когда веб-сервер после выполнения 
# согласования содержимого на основе сервера не находит контент, 
# соответствующий критериям, заданным агентом пользователя.

407 Proxy Authentication Required
# Это похоже на 401, но проверка подлинности необходима прокси.

408 Request Timeout
# Этот ответ отправляется на незанятое соединение некоторыми 
# серверами, даже без какого-либо предыдущего запроса клиентом. 
# Это означает, что сервер хотел бы отключить это неиспользуемое 
# соединение. Этот ответ используется гораздо больше, поскольку 
# некоторые браузеры, такие как Chrome, Firefox 27+ или IE9, 
# используют механизмы предварительного подключения HTTP для 
# ускорения серфинга. Также обратите внимание, что некоторые 
# серверы просто закрывают соединение без отправки этого сообщения.

409 Conflict
# Этот ответ отправляется, когда запрос конфликтует с текущим 
# состоянием сервера.

410 Gone
# Этот ответ будет отправлен, если запрошенный контент был удален 
# с сервера без адреса пересылки. Ожидается, что клиенты удалят 
# свои кеши и ссылки на ресурс. Спецификация HTTP предназначена 
# для того, чтобы этот код состояния использовался для 
# «ограниченного времени, рекламных услуг». API не должны вынуждены 
# указывать ресурсы, которые были удалены с помощью этого кода 
# состояния.

411 Length Required
# Сервер отклонил запрос, потому что поле заголовка Content-Length 
# не определено и сервер требует его.

412 Precondition Failed
# Клиент указал предварительные условия в своих заголовках, 
# которые сервер не встречает.

413 Payload Too Large
# Объект запроса больше ограничений, определенных сервером; 
# сервер может закрыть соединение или вернуть поле заголовка 
# Retry-After.

414 URI Too Long
# Запрошенный клиентом URI длиннее, чем сервер готов 
# интерпретировать.

415 Unsupported Media Type
# Формат медиаданных запрашиваемых данных не поддерживается 
# сервером, поэтому сервер отклоняет запрос.

416 Requested Range Not Satisfiable
# Диапазон, указанный поле заголовка Range в запросе, не может 
# быть выполнен; возможно, что диапазон находится вне размера 
# данных целевого URI.

417 Expectation Failed
# Этот код ответа означает, что ожидание, указанное полем 
# заголовка запроса Expect, не может быть выполнено сервером.

418 I'm a teapot                                    		'
# Сервер отказывается от попытки заварить кофе с чайником.

421 Misdirected Request
# Запрос был направлен на сервер, который не может дать ответ. 
# Это может быть отправлено сервером, который не настроен для 
# получения ответов на комбинацию схемы и полномочий, которые 
# включены в URI запроса.

422 Unprocessable Entity
# Запрос был хорошо сформирован, но из-за семантических ошибок 
# его не удалось выполнить.

423 Locked
# Доступ к ресурсу заблокирован.

424 Failed Dependency
# Запрос не выполнен из-за отказа предыдущего запроса.

426 Upgrade Required
# Сервер отказывается выполнять запрос с использованием 
# текущего протокола, но может захотеть сделать это после 
# того, как клиент обновится до другого протокола. Сервер 
# отправляет заголовок Upgrade в ответе 426, чтобы указать 
# требуемый протокол (протоколы).

428 Precondition Required
# Сервер происхождения требует, чтобы запрос был условным. 
# Предназначен для предотвращения проблемы «потерянного 
# обновления», когда клиент получает состояние ресурса, 
# изменяет его и выдает его обратно на сервер, когда третье 
# лицо изменило состояние на сервере, что привело к конфликту.

429 Too Many Requests
# Пользователь отправил слишком много запросов за определенный 
# промежуток времени («ограничение скорости»).

431 Request Header Fields Too Large
# Сервер не желает обрабатывать запрос, потому что его поля 
# заголовка слишком велики. Запрос МОЖЕТ быть повторно отправлен 
# после уменьшения размера полей заголовка запроса.

451 Unavailable For Legal Reasons
# Пользователь запрашивает незаконный ресурс, такой как 
# веб-страница, подвергнутая цензуре со стороны правительства.



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
5xx Ошибка сервера (Server Error)
# Информирование о случаях неудачного выполнения операции по вине 
# сервера. Для всех ситуаций, кроме использования метода HEAD, 
# сервер должен включать в тело сообщения объяснение, которое 
# клиент отобразит пользователю.

500 Internal Server Error
# Сервер столкнулся с ситуацией, когда он не знает, как обращаться.

501 Not Implemented
# Метод запроса не поддерживается сервером и не может быть 
# обработан. Единственными методами, которые необходимы серверам 
# для поддержки (и, следовательно, не должны возвращать этот код), 
# являются GET и HEAD.

502 Bad Gateway
# Этот ответ об ошибке означает, что сервер, работая в качестве 
# шлюза для получения ответа, необходимого для обработки запроса, 
# получил неверный ответ.

503 Service Unavailable
# Сервер не готов обрабатывать запрос. Общими причинами являются 
# сервер, который отключен для обслуживания или перегружен. Обратите 
# внимание, что вместе с этим ответом следует отправить удобную для 
# пользователя страницу, объясняющую проблему. Эти ответы должны 
# использоваться для временных условий, а заголовок 
# Retry-After: HTTP должен, по возможности, содержать расчетное 
# время до восстановления службы. Веб-мастер также должен следить 
# за заголовками, связанными с кешированием, которые отправляются 
# вместе с этим ответом, так как эти временные ответы обычно 
# не кэшируются.

504 Gateway Timeout
# Этот ответ об ошибке предоставляется, когда сервер действует как 
# шлюз и не может получить ответ вовремя.

505 HTTP Version Not Supported
# Версия HTTP, используемая в запросе, не поддерживается сервером.

506 Variant Also Negotiates
# Сервер имеет внутреннюю ошибку конфигурации: прозрачное 
# согласование содержимого для запроса приводит к циклической 
# ссылке.

507 Insufficient Storage
# Сервер имеет внутреннюю конфигурационную ошибку: выбранный 
# вариант ресурса сконфигурирован для участия в прозрачном 
# согласовании контента и, следовательно, не является надлежащей 
# конечной точкой в ​​процессе согласования.

508 Loop Detected
# При обработке запроса сервер обнаружил бесконечный цикл.

510 Not Extended
# Для его выполнения требуются дополнительные расширения для 
# запроса.

511 Network Authentication Required
# Код состояния 511 указывает, что клиент должен пройти 
# аутентификацию, чтобы получить доступ к сети.