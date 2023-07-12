<script lang="ts">
  
  import moment from 'moment-timezone'

  /**
  * @type {String}
  */

  export let widthDatePicker = '100%';

  let today = moment(new Date()).tz("Europe/Paris").format("YYYY/MM/DD").replaceAll('/', '-')
  const date = {min: today};
	const selected = {required: true};

</script>

<input class="date-picker" style='width: {widthDatePicker}' type=date min={date.min} {...selected} bind:value={today}/>

<style>
  .date-picker {
    color: var(--color-text-medium);
    border: var(--border-height-regular) solid var(--color-disabled);
    border-radius: var(--color-disabled);
    padding: var(--spacing-2);
    height: 18px;
    min-width: 280px;
    font-family: var(--font-family-primary);
    border-radius: var(--small-radius);
  }
  .date-picker {
    font-size: var(--font-size-label-1);
    font-family: var(--font-family-primary);
  }

  .date-picker:focus {
    color: var(--color-primary);
  }

  .date-picker:focus-visible {
    outline: var(--border-height-regular) solid var(--color-highlight);
    outline-offset: -1px;
  }

  ::-webkit-calendar-picker-indicator {
    width: 100%;
    position: absolute;
    opacity: 0;
  }
</style>
