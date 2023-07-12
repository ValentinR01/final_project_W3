<script lang="ts">
  import Icon from '../atoms/Icon.svelte';
  import ArrowRightIcon from '../../assets/icons/ArrowRightIcon.svelte';
  import CircleIcon from '../../assets/icons/CircleIcon.svelte';

  export let rowElements;
    
  export let filters : Array<string | number | boolean>;

  export let elements : Array<any> = [];
  
  for (const rowElement of rowElements) {
    const element = Object.entries(rowElement).reduce((acc: any, [key, value]) => {
    if (filters.includes(key)) acc[key] = value;
    return acc;
    }, {});
    
    if (element.name.length > 30) {
      element.name = `${element.name.substr(0, 30)}...`
    }
    elements.push(element);
  };

</script>

<!-- TODO add exception if no user is asigned (except the admin) then show button to add one -->
{#each elements as row}
  <tr>
    {#each Object.entries(row) as [key,rowCell]}
      {#if key === 'has_high_priority' && rowCell === 1}
        <td>
          <Icon class="block-center" name="no-prio" color="var(--blue-base)" width="15" height="15">
            <CircleIcon />
          </Icon>
        </td>
      {:else if (key === 'has_high_priority' && rowCell === 0)}
        <td></td>
      {:else if (key === 'rush_received' && rowCell === 1)}
        <td>
          <Icon class="block-center" name="rush" color="var(--green)" width="15" height="15">
            <CircleIcon />
          </Icon>
        </td>
      {:else if (key === 'rush_received' && rowCell === 0)}
        <td>
          <Icon class="block-center" name="no-rush" color="var(--grey)" width="15" height="15">
            <CircleIcon />
          </Icon>
        </td>
      {:else if (key === 'captation_done' && rowCell === 1)}
        <td>
          <Icon class="block-center" name="captation" color="var(--green)" width="15" height="15">
            <CircleIcon />
          </Icon>
        </td>
      {:else if (key === 'captation_done' && rowCell === 0)}
        <td>
          <Icon class="block-center" name="no-captation" color="var(--grey)" width="15" height="15">
            <CircleIcon />
          </Icon>
        </td>
      {:else if (key === 'version')}
        <td>V.{rowCell}</td>
      {:else}
        <td>{rowCell}</td>
      {/if}
    {/each}
    <td> 
      <a href="">
        <Icon name="arrow" color="transparent">
          <ArrowRightIcon />
        </Icon> 
      </a> 
    </td>
  </tr>
{/each}

<style>
  tr {
    white-space: nowrap;
    text-transform: capitalize;
  }
  td {
    border-top: 1px solid var(--grey);
    padding: var(--spacing-3);
    white-space: nowrap;
  }
  tr td:last-child {
    padding: 0;
    vertical-align: middle;
  }
</style>