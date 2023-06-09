<script>
  /**
  * @type {Array<string>}
  */
  export let values;

  /**
  * @type {any}
  */
  export let cat;
</script>
  
{#each values as option}
  <input class="input__checkbox" type=checkbox id={option} value={option} name={cat}>
  <label class="label__checkbox text-preset-5" for={option}> {option} </label>
{/each}

<style>
  .input__checkbox:checked,
  .input__checkbox:not(:checked) {
    position: absolute;
    left: -9999px;
  }

  .input__checkbox:checked + .label__checkbox,
  .input__checkbox:not(:checked) + .label__checkbox {
    position: relative;
    padding-left: var(--spacing-3);
    padding-right: var(--spacing-3);
    cursor: pointer;
  }

  .input__checkbox:checked + .label__checkbox:before,
  .input__checkbox:not(:checked) + .label__checkbox:before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 13px;
    height: 13px;
    border: var(--border-height-regular) solid;
    border-color: var(--color-border);
    background: var(--white);
  }

  .input__checkbox:checked + .label__checkbox:after,
  .input__checkbox:not(:checked) + .label__checkbox:after {
    content: '';
    width: 13px;
    height: 13px;
    background: var(--blue-base);
    position: absolute;
    top: 1px;
    left: 1px;
    -webkit-transition: all 0.2s ease;
    transition: all 0.2s ease;
  }

  .input__checkbox:not(:checked) + .label__checkbox:after {
    opacity: 0;
    -webkit-transform: scale(0);
    transform: scale(0);
  }

  .input__checkbox:checked + .label__checkbox:after {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }
</style>