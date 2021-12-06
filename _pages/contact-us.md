---
permalink: /contact-us
layout: page
title: Contact us
---

<h2>
	This is our team members.
</h2>

<h4>
	Feel free to contact us!
</h4>

<ul>
	{% for member in site.data.members %}
	<li>
			<span> {{ member.name }} </span>
			<div>
				<span> Git-hub Repository </span>
				<a href="https://github.com/{{ member.github}}"> {{ member.github }}</a>
			</div>
			<div>
				<span> Email-Address </span>
				<a href="{{ member.email}}"> {{ member.email}} </a>
			</div>
	</li>
	{% endfor %}
</ul>