{% import 'macros.rst' as macros %}
{% macro auto_summary(objs, title='') -%}

.. list-table:: {{ title }}
   :header-rows: 0
   :widths: auto

{% for obj in objs %}
    * - obj.name
      - obj.summary
{% endfor %}
{% endmacro %}