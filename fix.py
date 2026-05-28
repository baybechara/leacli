import sys
content = open('Website/development/landing-page.html', 'r', encoding='utf-8').read()

new_faq = '''		<div class="uk-container uk-container-small uk-margin-large-top uk-margin-large-bottom">
			<h2 class="uk-text-center uk-text-bold uk-text-uppercase">Вопросы и ответы</h2>
			<ul class="uk-margin-remove" uk-accordion>
				<li class="uk-open">
					<a class="uk-accordion-title" href>Сколько времени занимает разработка Landing Page?</a>
					<div class="uk-accordion-content">
						<p>В среднем разработка качественного лендинга под ключ занимает от 14 до 25 дней. Сроки зависят от сложности дизайна, наличия исходных материалов (тексты, фото) и скорости согласования этапов. Если вам нужен сайт быстрее, мы можем использовать готовые UI-решения, что сократит срок до 7-10 дней.</p>
						<div class="accordion-footer">
							<div class="uk-grid-small uk-flex-middle uk-child-width-auto" uk-grid>
								<div>
									<a href="#modal" uk-toggle class="uk-button uk-button-primary uk-width-1-1">Оставить заявку</a></div>
								<div class="uk-width-expand"></div>
								<div>
									<a href="" target="_blank">
										<img src="/img/elements/whatsappdark.svg" width="40">
									</a>
								</div>
							</div>
						</div>
					</div>
				</li>
				<li>
					<a class="uk-accordion-title" href>Вы пишете тексты (копирайтинг) или нам нужно давать свои?</a>
					<div class="uk-accordion-content">
						<p>Мы полностью берем копирайтинг на себя. Перед началом работы мы проводим подробный бриф с вами или вашим отделом продаж, собираем всю фактуру о продукте, а затем наш маркетолог упаковывает это в продающие смыслы. Если у вас уже есть готовые тексты, мы можем взять их за основу и доработать под формат лендинга.</p>
						<div class="accordion-footer">
							<div class="uk-grid-small uk-flex-middle uk-child-width-auto" uk-grid>
								<div>
									<a href="#modal" uk-toggle class="uk-button uk-button-primary uk-width-1-1">Оставить заявку</a></div>
								<div class="uk-width-expand"></div>
								<div>
									<a href="" target="_blank">
										<img src="/img/elements/whatsappdark.svg" width="40">
									</a>
								</div>
							</div>
						</div>
					</div>
				</li>
				<li>
					<a class="uk-accordion-title" href>Смогу ли я сам редактировать контент после запуска?</a>
					<div class="uk-accordion-content">
						<p>Да, по вашему желанию мы можем интегрировать лендинг с удобной системой управления (CMS), такой как WordPress, или использовать интуитивные no-code платформы (Webflow, Tilda). Вы сможете легко менять тексты, цены и фото без привлечения программиста.</p>
						<div class="accordion-footer">
							<div class="uk-grid-small uk-flex-middle uk-child-width-auto" uk-grid>
								<div>
									<a href="#modal" uk-toggle class="uk-button uk-button-primary uk-width-1-1">Оставить заявку</a></div>
								<div class="uk-width-expand"></div>
								<div>
									<a href="" target="_blank">
										<img src="/img/elements/whatsappdark.svg" width="40">
									</a>
								</div>
							</div>
						</div>
					</div>
				</li>
			</ul>
		</div>'''

import re

# Find where the broken stuff starts. The last valid block before the broken part is the process tab section which ends around:
# 								</div>
# 							</div>
# 						</div>
# 					</div>
# 					<div class="uk-margin-medium-top uk-margin-medium-bottom"> 
# 					</div>

# Wait, looking at the git diff earlier, the mess starts after the end of the tabs section (line 427 `</section>`).
# So we can find `</section>` that closes `.dark-section`.
# Let's just find the closing `</section>` after the process tabs, and the opening `<section class="tariffs">`.
# Everything between them should be replaced with our `new_faq`.

parts = content.split('<section class="tariffs">')
if len(parts) == 2:
    part1 = parts[0]
    part2 = parts[1]
    
    # We want to keep up to `</section>` that closes `.dark-section`.
    # Let's find the last `</section>` in part1.
    last_section_end = part1.rfind('</section>')
    
    if last_section_end != -1:
        # Reconstruct content
        content = part1[:last_section_end + 10] + '\n\n' + new_faq + '\n\n\t\t<section class="tariffs">' + part2
        open('Website/development/landing-page.html', 'w', encoding='utf-8').write(content)
        print("Success")
    else:
        print("Failed to find </section>")
else:
    print("Failed to find <section class='tariffs'>")
