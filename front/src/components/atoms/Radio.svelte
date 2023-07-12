<script>
  /**
  * @type {Array<string>}
  */
  export let values;

  /**
  * @type {String}
  */
  export let cat;

  export let valueSelected = values[0];
</script>

<div class='radio'>
  {#each values as option}
    <input class="input-radio" type=radio id={option} value={option} name={cat} bind:group={valueSelected}>
    <label class="label-radio text-preset-5" for={option}> {option} </label>
  {/each}
</div>

<style>
  .radio{
    display: flex;
    flex-wrap: wrap;
    row-gap: var(--spacing-2);
  }

  .label-radio{
    width: 150px;
  }

  .input-radio:checked,
  .input-radio:not(:checked) {
    position: absolute;
    left: -9999px;
  }

  .input-radio:checked + .label-radio,
  .input-radio:not(:checked) + .label-radio {
    position: relative;
    padding-left: var(--spacing-3);
    padding-right: var(--spacing-3);
    cursor: pointer;
  }

  .input-radio:checked + .label-radio:before,
  .input-radio:not(:checked) + .label-radio:before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 13px;
    height: 13px;
    border: var(--border-height-regular) solid;
    border-color: var(--color-border);
    border-radius: 100%;
    background: var(--white);
    -webkit-transition: border-color 0.3s ease;
    transition: border-color 0.3s ease;
  }

  .input-radio:checked + .label-radio:after,
  .input-radio:not(:checked) + .label-radio:after {
    content: '';
    width: 13px;
    height: 13px;
    background: var(--blue-base);
    position: absolute;
    top: 1px;
    left: 1px;
    border-radius: 100%;
    -webkit-transition: all 0.1s ease;
    transition: all 0.1s ease;
  }

  .input-radio:not(:checked) + .label-radio:after {
    opacity: 0;
    -webkit-transform: scale(0);
    transform: scale(0);
  }

  .input-radio:checked + .label-radio:after {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }

  .input-radio:checked + .label-radio:before{
    border-color: var(--blue-base);
  }
</style>