<script>
  export let marginTop = '0px';
  export let marginBottom = '0px';
  export let marginLeft = '0px';
  export let marginRight = '0px';
</script>

<div 
  style='margin-top: {marginTop}; margin-bottom: {marginBottom}; margin-left: {marginLeft}; margin-right: {marginRight}'>
  <slot></slot>
</div>
  