<script lang="ts">
  
  import moment from 'moment-timezone'

   /**
  * @type {String}
  */

  let today = moment(new Date()).tz("Europe/Paris").format("YYYY/MM/DD").replaceAll('/', '-')
  const date = {min: today};
	const selected = {required: true};

</script>

<input type=date min={date.min} {...selected} bind:value={today}/>
