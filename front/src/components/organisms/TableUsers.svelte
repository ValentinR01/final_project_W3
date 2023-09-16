<script lang="ts">
	import TableRowUsers from '../molecules/TableRowUsers.svelte';
  import Icon from '../atoms/Icon.svelte';
  import SortArrowIcon from '../../assets/icons/SortArrowIcon.svelte';

	export let selectedRowElements : any;

  const tableHeaders = Object.keys(selectedRowElements[0])

  let selectedHeader = "";
  let ascendingOrder = true;

  const sortByString = (colHeader: any) => {
    selectedRowElements = selectedRowElements.sort((obj1: any, obj2: any) => {
      if (obj1[colHeader] < obj2[colHeader]) {
          return -1;
      } else if (obj1[colHeader] > obj2[colHeader]) {
        return 1;
      }
      return 0;	
    });
    if (!ascendingOrder) {
      selectedRowElements = selectedRowElements.reverse()
    }
    selectedHeader = colHeader;
  }
</script>

<table>
	<thead>
    <tr> 
      {#each tableHeaders as header}
      <th on:click={() => sortByString(header)}>
        <button on:click={() => ascendingOrder = !ascendingOrder}>
          {header
          .replace("profile_pic", "Photo")
          .replace("fullname", "Nom")
          .replace("email", "Email")
          .replace("domain", "Métier")
          .replace("role", "Rôle")}
          <span>
            <Icon color="var(--darker-grey)" width="10" height="12">
              <SortArrowIcon />
            </Icon>
          </span>		
        </button>	
      </th>
      {/each}
    </tr>
  </thead>
  <tbody>
	  <TableRowUsers {selectedRowElements}/>
	</tbody>
</table>

<style>
  tr {
    white-space: nowrap;
  }
  th {
    padding-bottom: var(--spacing-3);
    padding-left: var(--spacing-4);
    padding-right: var(--spacing-4);
    text-align: left;
  }
  th:first-child {
    padding-left: 0;
  }
  span {
    display: inline-block;
    vertical-align: middle;
    margin-left: var(--spacing-1);
  }
  button {
    cursor: pointer;
    border: none;
    margin: 0;
    padding: 0;
    width: auto;
    overflow: visible;
    background: transparent;
    color: var(--darker-grey);
    font: inherit;
    line-height: normal;
    -webkit-font-smoothing: inherit;
    -moz-osx-font-smoothing: inherit;
    -webkit-appearance: none;
  }
</style>